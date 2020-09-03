#!/usr/local/bin/python3 

from subprocess import Popen, PIPE
from urllib.parse import quote
import sqlite3, datetime, sys, re

# Global Variables
removeCheckedItems = True # Set to false if you want to keep "completed" to-do items when this is run
bearDbFile = str(sys.argv[3])
oneTabID = str(sys.argv[4])

# Methods
def create_connection(db_file): # Establish SQLITE database connection cursor
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("Failed to establish connection")
        return None

    return conn

def xcall(url): # Simple wrapper method to run xcalls
    r = Popen(['/Applications/xcall.app/Contents/MacOS/xcall',
        '-url', f'"{url}"'
        ], stdout=PIPE)

    stdout = r.communicate()
    return str(stdout[0].decode('utf-8')).strip().replace(" ","")

def getOneTab(): # Get and return OneTab note from Bear
    bearNote = bear.execute(f"SELECT * FROM ZSFNOTE WHERE ZUNIQUEIDENTIFIER IS '{oneTabID}'").fetchone()
    return str(bearNote[32]) # ZTEXT

def updateOneTab():
    oneTab = getOneTab().replace("# BearMarks","")
    if removeCheckedItems:
        oneTab = re.sub(r"^\+ .*\n","",oneTab,flags=re.MULTILINE)
        oneTab = re.sub(r"^\#\#\# .*\n\n","",oneTab,flags=re.MULTILINE)

    if url in oneTab:
        #print("URL already present. Skipping.")
        return 

    now = datetime.datetime.now().strftime("%B %d, %Y")   
    prefix = f'### {now}\n'
    line = f'- [{title}]({url})'

    if prefix in oneTab:  
        oneTab = oneTab.replace(prefix,f'{prefix}{line}\n')
    else:
        line = f'{prefix}{line}\n'
        oneTab = line + oneTab    

    update = f'bear://x-callback-url/add-text?id={oneTabID}&mode=replace&text={quote(oneTab.strip())}&open_note=no'
    xcall(update)

# Main functionality:
if __name__ == '__main__':
    title = sys.argv[1]
    url = sys.argv[2]

    # Connect to Bear database
    beardb = create_connection(bearDbFile)
    bear = beardb.cursor()

    # Process tab and update database:
    updateOneTab()