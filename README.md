# saveTabToBear
Alfred workflow to save current Chrome tab to a Bear note for later reference. It requires python3 and [xcall.app](https://github.com/robwalton/python-xcall), created by Martin Finke and included in this repository.


## Preparation
You can either clone this repository on your local machine using:

`git clone https://github.com/vinceblake/saveTabToBear.git`

Or you can download the .zip file directly and extract it. 

Place `onetabtobear.py` file and `xcall.app` somewhere safe. Anywhere you like is fine but they'll need to live there permanently. You'll also need to reference their locations in a moment.

---

Open up your Bear application and create a new note. The first line should look something like this (call it what you want, but remember the title):

![img](https://github.com/vinceblake/saveTabToBear/raw/master/screenshots/noteTitle.png)

Now that we've got our title, we'll need our note's unique identifier. Click the three dots in the upper right of the note and select `Copy Note's Identifier`:

![img](https://github.com/vinceblake/saveTabToBear/raw/master/screenshots/copyID.png)

## Installation
With the above steps complete, simply double-click the `.alfredworkflow` file to import it into Alfred. You'll be greeted with a screen that looks something like this:

![img](https://github.com/vinceblake/saveTabToBear/raw/master/screenshots/alfredVars.png)

You will need to update these variables for this to work
* bearDbFile: Where your [Bear notes database](https://bear.app/faq/Where%20are%20Bear's%20notes%20located/) is located. This will almost certainly be `/Users/[YOUR USERNAME]/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/database.sqlite`
* bearNoteID: The unique identifier you copied above. Just paste it in here.
* bearNoteTitle: I call it BearMarks. You can call it whatever you like. Just make sure it matches what you created in the Preparation steps. 
* scriptLocation: Wherever you chose to place the onetabtobear.py file. 
* xCallApp: Wherever you chose to place the xcall.app directory. I like having it in my Applications folder, but it can be run from anywhere.
