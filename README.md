# archivesspace-skill-share
Scripts used at Beyond the Basics ArchivesSpace Skill Share on Oct. 17

##Sample Files
####[thecaptains.json](thecaptains.json)
A sample file of JSON data that can be used with the [postAgents.py](postAgents.py) script to create ArchiveSpace Agent records via the ArchivesSpace API.

#Sample Scripts
####[postAgents.py](postAgents.py)
This script differs from the [postArchivalObjects.py](postArchivalObjects.py) script because it posts new records to ArchivesSpace rather than overwriting existing records based on their "uri."  This script requires a JSON file of agent data to be placed in the same directory as the script you will be running, in this case, the agent data is contained in "thecaptains.json."  This JSON file contains the minimum number of properties that are required to create an agent record through the API.  If you try POST to a JSON file that does that conform to ArchivesSpace's requirements, the API will provide an error message that details what required properties are missing.

####[getArchivalObjects.py](getArchivalObjects.py)
You can try this easy script (which makes no changes to any data). This script will authenticate with the API and then download all of ArchiveSpace's archival objects to a JSON file called "archival_objects.json." 

Note: The "page_size" is set to 3000, but ArchivesSpace's configuration defaults to 250 .
To set this within the demo, go to Files (looks like a file drawer) > archivesspace > config and look for the lines that say 

\#AppConfig[:default_page_size] = 10

\#AppConfig[:max_page_size] = 250

(Note that a # in this case comments these lines out, so you must remove the # to enable this configuration). 

####[postArchivalObjects.py](postArchivalObjects.py)
After downloading the archival objects to a JSON file "archival_objects.json" with the [getArchivalObjects.py](getArchivalObjects.py) script, users can edit the JSON file and post the changes back into ArchivesSpace using this [postArchivalObjects.py](postArchivalObjects.py) script. The "archival_objects.json" file needs to be in the same directory as [postArchivalObjects.py](postArchivalObjects.py) for the script to work. The script matches each archival object based on the "uri" property and overwrites the current ArchivesSpace archival object record with the archival object record contained in the "archival_objects.json."  The "lock_version" will also need to match between the two archival objects records or the record will not be overwritten. The lock version changes every time you modify the record to prevent users from overwriting new data with old data. This built-in failsafe is a good one, but it is something to remember and plan for.


