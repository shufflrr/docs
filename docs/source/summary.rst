Summary
=======

What is Shufflrr's API?
-----------------------

Shufflrr’s API offers a wide variety of actions to allow your team to integrate multiple systems with Shufflrr to cover a range of use cases.  

What systems can I integrate with Shufflrr’s API?
-------------------------------------------------

Any system that can call APIs can integrate with Shufflrr’s APIs.

.. image:: /img/Integrations.png

Some of the systems that our customers have integrated with Shufflrr APIs include:

- SalesForce
- SharePoint
- Google Drive
- Veeva
- DropBox
- Box.com

What can I use Shufflrr’s API for?
----------------------------------

These are just a few use cases that our customers have used Shufflrr’s API for:

- Recreating folder structure in Shufflrr to replicate your system structure
- Uploading files from your system into Shufflrr
- Downloading files from Shufflrr into your system
- Updating data in Shufflrr from your system
- Updating your system with data from Shufflrr
- Importing reporting information from Shufflrr into your system for reporting
  and analytics

Purpose
-------

The purpose of this documentation is to provide information on the core Shufflrr
API endpoints so your team can easily integrate your system(s) with Shufflrr.

What is an API
===============

API stands for **A**\ pplication **P**\ rogramming **I**\ nterface.  Using an API allows for one system (in this case your system like SharePoint, SalesForce, Google Drive, Veeva, Box, Dropbox, etc) to interface with another system (in this case Shufflrr).  Examples of use cases are:

- Recreating folder and file structure in Shufflrr as in your system
- Uploading files from your system into Shufflrr
- Downloading files from Shufflrr into your system
- Updating data in Shufflrr
- Updating your system with data from Shufflrr
- Importing reporting information from Shufflrr into your system for reporting and analytics

What type of APIs does Shufflrr use?
=====================================

Shufflrr uses REST (\ **RE**\ presentational **S**\ tate **T**\ ransfer) architecture for our APIs.  
Requests (what you send to Shufflrr API) and responses (what Shufflrr sends back to you) are formatted in 
JSON (\ **J**\ ava\ **S**\ cript **O**\ bject **N**\ otation).  You can read more about REST API architecture on the `Wikipedia page for REST`__.  To learn more about JSON and its format you can read more on `JSON.org`__.

.. __: https://en.wikipedia.org/wiki/Representational_state_transfer

.. __: https://www.json.org/json-en.html

Parts of an API call
====================

When calling an API (sending a request) there are 6 main pieces that need to be defined:

- **Method** – What type of action you are trying to accomplish
- **EndPoint** – The URL you are calling to perform the action
- **Parameters** – These are values that are sent in as part of the URL string
- **Authentication** – This is how your application will get authorized with Shufflrr to allow your system to perform the desired actions
- **Header** – These are metadata values used to give instructions or settings to Shufflrr for acting upon the desired method with the specified request (body)
- **Body** – This is the information on the requested action to be performed.  This is sometimes referred to as a payload.

When information is returned from the call to an API the data that is returned is called a Response.  The information returned in the Response Body is sent back in JSON format as well.  This information can then be parsed and used in your application.

API Request Methods
--------------------

The APIs used in Shufflrr use the following methods:

- :blue:`GET` – Requests data from Shufflrr. This is the most common type of request. 
- :green:`POST` – This is generally used to submit a form or to create a new object in Shufflrr.
- :orange:`PUT` – This is generally used to update an existing object in Shufflrr.
- :red:`DELETE` – This is used to remove an object from Shufflrr.

Complete list of Shufflrr’s API EndPoints
--------------------------------------------

Shufflrr’s API is documented in Swagger and can be found at `https://wwwapi.shufflrr.com/api`__.  

.. note:: 

 to use the APIs for your specific portal you should replace wwwapi with your specific subdomain (portal name).   
 
 For example, if your Shufflrr portal is ABC123.shufflrr.com you would replace wwwapi with ABC123 for all the API calls, headers, and links in the payload (body).

.. __: https://wwwapi.shufflrr.com/api


Authentication
---------------

All calls to Shufflrr APIs need to be authenticated.  Before calling other APIs the first call that will need to be made is to the Login API.  The Login API will return a cookie that should be used by all other API calls to allow them to be authenticated and authorized to perform the desired action.

Header
-------

For most of the Get APIs, no headers are required to be set but it is recommended to set:  

+--------------+------------------+
| Key          | Value            |
+==============+==================+
| Content-Type | application/json |
+--------------+------------------+

For other calls (puts, posts, deletes) the following headers should be set: 

+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Key                              | Value                                                                                                                              |
+==================================+====================================================================================================================================+
| Accept-Encoding                  | gzip, deflate, br                                                                                                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Accept-Language                  | en-US,en;q=0.9                                                                                                                     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Access-Control-Allow-Credentials | true                                                                                                                               |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Access-Control-Allow-Origin      | `https://wwwapi.shufflrr.com`__                                                                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Content-Type                     | application/json                                                                                                                   |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Origin                           | `https://wwwapi.shufflrr.com`__                                                                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| User-Agent                       | Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.120 Safari/537.36 Vivaldi/2.3.1440.57 |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Accept                           | application/json, text/javascript, */*; q=0.01                                                                                     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Referer                          | `https://wwwapi.shufflrr.com/Shufflrr`__                                                                                           |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| X-Requested-With                 | XMLHttpRequest                                                                                                                     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. __: https://wwwapi.shufflrr.com

.. __: https://wwwapi.shufflrr.com

.. __: https://wwwapi.shufflrr.com/Shufflrr


Body
-----

The Body of a request is not used in GET Methods.  It is only used in POST, PUT, & DELETE methods.  The body is specific to each individual call but each request body must be specified in JSON format.

Getting Help from Shufflrr
==========================

If you have additional questions on the APIs or need details for functionality not covered in the Core APIs, please contact our technical support.  You can access this when logged into your Shufflrr portal and clicking on the ‘**?**’ 

.. image:: /img/help.png

When the ‘**How can we help?**’ dialogue box appears, click on the link for ‘**Technical Support**’.  Fill out text area with your question and details.  Then click on the save button.

.. image:: /img/howcanwehelp.png

Getting started
================

Best practices are to have a separate group and users dedicated to API connections.  It is also recommended to have a separate user for each connecting system.  Furthermore, it will keep API connections and their activities separate from everyday Shufflrr end-user activities.  

Setup a group for the API user to use.  After you log into Shufflrr go to the '**Admin**' section and then click on the '**Groups**' Tab and click on ‘**Add Group**’ button.

.. image:: /img/group.png

In the ‘**Add Group**’ dialogue box type in the ‘**API Users**’ for the group name and type in a description so that admins of the portal know not to use this group for any users that are not using the API.  Click the '**Add Group**' button.

.. image:: /img/addgroup.png

In the group configuration pane check the boxes next to the rights you want your API user to have the rights to perform.  For most use cases the below settings would cover the needed rights.  Then click on '**Update**'.

.. image:: /img/permissions.png

Next, setup a user in your portal to be used for the API calls.  Still in the '**Admin**' section, click on the '**Users**' tab click on the '**add**' button.

.. image:: /img/user.png

In the '**Add User**'' dialogue box Type in *API* for the first name, *User* for the last name, and provide an email address.  **Note:** You cannot use an email address of an existing user as users are identified by their email address.  Click on the '**Add User**' button.

.. image:: /img/adduser.png

After the user is added to your Shufflrr portal, click on the API User in the user list.  Then in the user detail area, click on the '**Reset Password**' button to send an email to the address specified for the user.  The email will contain a link for the password to be set for the API User.

.. image:: /img/resetpassword.png

After you set the password for the API User account, go back to the Shufflrr portal and on the API User account, click on the '**Groups**' tab.  Check the box next to ‘**API Users**’ and click the '**Save**' button.

.. image:: /img/assigngroup.png

**The API user will only be able to act upon folders (and files in them) that they have access to.  Therefore the API user(s) will need permissions to the folders that the API user will affect.**

**If you have existing folders in your Shufflrr portal** (that you want to be able to manage through the APIs) make sure to set the permissions to allow for the API Users group to have access to them.  
In Shufflrr click on the down arrow next to each folder you want to modify the permissions on and click on ‘**Permissions**’ from the menu.

.. image:: /img/folderpermissions.png

In the '**Folder Permissions**' dialogue box, type in *API Users* and select the *API Users* group.  Change the Permission Level to *Full Control* and click on the '**Add a permission**' button.  Then click on the '**Apply to Child Folders**' button to give permissions to the folders under the one you are updating the permissions on.

.. image:: /img/addpermissions.png

When a new folder is created in the Shufflrr front end be sure to provide to grant access to the needed API user(s).  When it is created using the API the rights will be set on the folder automatically.

Get familiarized with the APIs
------------------------------

We recommend that your developer use a tool like `postman`__ to test out and familiarize themselves with the APIs before they start coding the solution.

.. __: https://www.postman.com/

Core APIs
----------

This section will cover the core functionality for interfacing with the Shufflrr APIs.  

Core API Details
-----------------

When calling the APIs there are some pieces of data that will be returned in the response body that you will either use to make subsequent calls to other APIs or you can store in your calling system so that you do not have to perform some GET APIs to get the IDs for some elements.  Each API call will point out which data points will be used with other API calls.

Login
~~~~~~

In order for Shufflrr to validate your API user has the rights to perform the actions, the account must login.  To interface with the Shufflrr APIs the first step is to authenticate the session by using the Account Login API.  This API is used to send in a specific user (API User).  This API will validate that the account has access to your Shufflrr portal.  A successful call will return a cookie which will need to be used in subsequent calls to other APIs to validate that the session is authenticated and authorized. 

This is a :green:`POST` method

The Login API can be found at:

`https://wwwapi.shufflrr.com/api/account/login`__

.. __: https://wwwapi.shufflrr.com/api/account/login

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Account/Account_Login`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Account/Account_Login

Sample Request Body
###################

::

   {
    "emailAddress": "APIUser@shufflrr.com",
    "password": "Password",
    "keepLoggedIn": true
   }

Replace the email and password in the above request body with the email and password for the API User account you setup in the steps above.

Successful Login
##################

When a login is successful the success element in the response body will be set to true.  From the response body capture these pieces of data that will be used in other API calls:

- portalId (in the user element) - This is the ID of your Shufflrr portal.
- id (in the user element) – this is the ID of the API User.

Login Failure
##############

When a login fails the success element in the response body will be set to false.

Get All Folders
~~~~~~~~~~~~~~~~

To get a list of all Folders in the Shufflrr portal use the All Folders API.

This is a :blue:`GET` method

The All Folders API can be found at:

`https://wwwapi.shufflrr.com/api/folders/all`__

.. __: https://wwwapi.shufflrr.com/api/folders/all

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_All`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_All

Match up on the folder name (and position in the folder tree) to capture the id of the folder to be used in other API calls.

Create Folder
~~~~~~~~~~~~~~

To create a new folder in Shufflrr call the Create Folder API.  Make sure to set the parentFolderId to the Folder ID that want the new folder created in.

This is a :green:`POST` method

The Create Folder API can be found at:

`https://wwwapi.shufflrr.com/api/folders`__

.. __: https://wwwapi.shufflrr.com/api/folders

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Post`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Post

Sample Request Body
###################

::

    {
     "fileType": "Folder",
     "isFolder": true,
     "isFollowedByCurrentUser": true,
     "userPermissions": "16777215",
     "id": 0,
     "name": "New Folder Name",
     "description": "This is the description for my folder",
     "createdDate": "2020-10-21T12:48:10.504Z",
     "modifiedDate": "2020-10-21T12:48:10.504Z",
     "createdById": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
     "createdByName": "API User",
     "modifiedById": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
     "modifiedByName": "API User",
     "parentFolderId": XXXXXXXX,
     "portalId": 2261101,
     "deleted": false
    }
	
.. note:: 
 Keep id set to 0 in the request body.  Shufflrr will assign an ID when it creates the folder
 
Make sure to replace the values in the above Request Body with the appropriate Values:

+---------------------+-------------+------------------------------------------------------------+
| Request Body Value  | API call    | Value or Element(s) to use from API call                   |
+=====================+=============+==============+=============================================+
| name                | N/A         | Use the name of the folder from your sending system        |
+---------------------+-------------+------------------------------------------------------------+
| description         | N/A         | Use the description of the folder from your sending system |
+---------------------+-------------+------------------------------------------------------------+
| createdDate         | N/A         | Use the current date and time                              |
+---------------------+-------------+------------------------------------------------------------+
| modifiedDate        | N/A         | Use the current date and time                              |
+---------------------+-------------+------------------------------------------------------------+
| createdById         | Login       | id                                                         |
+---------------------+-------------+------------------------------------------------------------+
| modifiedById        | Login       | id                                                         |
+---------------------+-------------+------------------------------------------------------------+
| parentFolderId      | All Folders | id                                                         |
+---------------------+-------------+------------------------------------------------------------+
| portalId            | Login       | portalId                                                   |
+---------------------+-------------+------------------------------------------------------------+

If you wish to store the ID of folders when they are created, use the id returned in the response body for each folder.

Get Folder Contents
~~~~~~~~~~~~~~~~~~~~

To get information all of the contents of a folder (sub folders and files) call the Get Folder Contents API.

This is a :blue:`GET` method

The Get Folder Contents API can be found at:

`https://wwwapi.shufflrr.com/api/folders/{id}/contents`__

.. __: https://wwwapi.shufflrr.com/api/folders/{id}/contents

Where **{id}** is the Folder ID to get the contents of

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Contents`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Contents

Update existing folder name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To rename an existing folder to another name use the folders API.  The ID is the ID of the folder you are looking to rename.

This is a :orange:`PUT` method.

The folders API can be found at:

`https://wwwapi.shufflrr.com/api/folders`__

.. __: https://wwwapi.shufflrr.com/api/folders

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Put`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Put

Sample Request Body
####################

::

 {
  "id": 0,
  "name": "New Folder Name"
 }
 
Replace 0 with the ID of the folder you want to rename and the name value with the name you want the folder set to.

Move folder
~~~~~~~~~~~

To move a folder and all its contents use the Folder Move API.  You will need to replace the {id} in the URL path with ID of the folder you want to move.  The request body will contain just the ID of the folder you want the folder you are moving to be under.  

This is a :green:`POST` method

The move folder API can be found at:

`https://wwwapi.shufflrr.com/api/folders/{id}/move`__

.. __: https://wwwapi.shufflrr.com/api/folders/{id}/move

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Move`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Move

Sample Request Body
####################

To move the folder under another folder
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

::

 0
 
Replace 0 with the folder ID you want to move the folder under. Note that this request body does not have the curly brackets around the data and only includes the folder ID to move the folder under.

To move the folder to be a root folder
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

::

 {
  "bodyData": null
 }

Remove folder
~~~~~~~~~~~~~~~

To remove a folder and all its contents use the folder delete method.  The id in the path will be the ID of the folder you want to remove (retrieved from one of the previous calls in Get list of folders section).

This is a :red:`DELETE` method

The delete folder API can be found at:

`https://wwwapi.shufflrr.com/api/folders/{id}`__

.. __: https://wwwapi.shufflrr.com/api/folders/{id}

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Delete`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Delete

Additional Headers
###################

These Headers need to be added to the ones specified at the top of this document for this call

+----------------+------------------+
| Key            | Value            |
+================+==================+
| Sec-Fetch-Site | same-origin      |
+----------------+------------------+
| Sec-Fetch-Mode | cors             |
+----------------+------------------+
| Sec-Fetch-Dest | empty            |
+----------------+------------------+

Sample Request Body
###################

::

 {}

Upload File
~~~~~~~~~~~~

To add a new file (presentation, video, images, documents, etc) use the folder upload API.  The ID in the path is the ID of the folder that you want to upload the file into.  Replace the {id} element in the url below with the id of the folder you want to upload the file into.

Shufflrr uses the Windows method of file management.  When a file is uploaded to a folder and it has the same filename and extension it will be considered an update to the file.  For updating an existing file this same method will be used to upload the file to update to the same folder it exists in with the same filename.

This is a :green:`POST` method

The folder upload API can be found at:

`https://wwwapi.shufflrr.com/api/folders/{id}/upload`__

.. __: https://wwwapi.shufflrr.com/api/folders/{id}/upload

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Upload`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Folders/Folders_Upload

To test this API with postman you will need to set specific headers and settings (these settings will also need to be set in your code to interface with the API).   Headers are listed in the Headers section above in this document.

In Postman click on Body and then:

Change the format dropdown to be form-data

.. image:: /img/formdata.png
 
For the first record, inside the key field hover your mouse over the right-hand side and a dropdown will appear.  
It is defaulted to Text.  
Click it and choose File.  
This will cause a Select Files button to appear in the Value Field.

.. image:: /img/fileselect.png
 
Click the button and browse to the file to be uploaded.

Once this is selected, you can submit the request send the request to upload the file.

Sample Successful Upload 
#########################

::

 [
  {
   "filename": "filename.xxx",
   "error": null,
   "complete": true
  }
 ]
 
Sample Failed Upload
#####################

::
	
 An error occurred uploading the file.

Get Actions Queue
~~~~~~~~~~~~~~~~~

After uploading a file, it will be loaded into a queue.  The uploadedFileId of the file will not be created until the file has been processed and stored in Shufflrr.  When files are first sent in, the queue will show them with actionType set to "ProcessUploadedFileAction" and the status is set to "New".  :red:`DO NOT` use the ID element because the ID in the queue is temporary; it is not the final file ID in Shufflrr.  

Once the file is processed in Shufflrr, it will then get it’s uploadedFileId.  The uploadedFileId element is the ID for the file you uploaded matching on:

- file name 
- folder id uploaded to
- actiontype value of “ProcessUploadedFileAction” 
- status value of “CompletedSuccess”

The file information will remain in the queue for 24 hours or until a user Dismisses the file from the queue in the Shufflrr UI.

This is a :blue:`GET` method

The Get Actions Queue API can be found at:

`https://wwwapi.shufflrr.com/api/actionsqueue`__

.. __: https://wwwapi.shufflrr.com/api/actionsqueue

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/ActionsQueue/ActionsQueue_Get`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/ActionsQueue/ActionsQueue_Get

If you wish to store the ID of files as they process use the uploadedFileId value.

Get list of files
~~~~~~~~~~~~~~~~~~

To get a list of all files (presentation, video, images, documents, etc) use the get files API.  Sending the request without any parameters will return all the files in the portal.

This is a :blue:`GET` method

The get files API can be found at:

`https://wwwapi.shufflrr.com/api/files`__

.. __: https://wwwapi.shufflrr.com/api/files

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Get`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Get

If you wish to match up on parentFolderId and name and store the id value for the specific file

Get File
~~~~~~~~~

To get the detailed information on a specific file call the Get File API.  Replace the {id} in the url below with the file id that you want to get the information on.

This is a :blue:`GET` method.

The get file API can be found at:

`https://wwwapi.shufflrr.com/api/files/{id}`__

.. __: https://wwwapi.shufflrr.com/api/files/{id}

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Get_0`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Get_0

Update information on an existing file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update information on a file that was previously uploaded (File Name & Description), use the update files API.  The ID in the Body of the request is the ID of the file to change the information on.  

This is a :orange:`PUT` method.

The update files API can be found at:

`https://wwwapi.shufflrr.com/api/files`__

.. __: https://wwwapi.shufflrr.com/api/files

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Put`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Put

Sample Request Body
####################

::

 {
  "id":0,
  "name":"NewFileName.pptx",
  "description":"New description"
 }
 
Replace 0 with the file ID you want to apply the new file name and description to.  Specify the file name and description that you want updated on the file

Move a file
~~~~~~~~~~~~

To move a file into a different folder, use the move files API 

This is a :green:`POST` method.

The move files API can be found at:

`https://wwwapi.shufflrr.com/api/files/move`__

.. __: https://wwwapi.shufflrr.com/api/files/move

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Move`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Move

Sample Request Body
###################

::

 {
  "fileIds": [
   X
  ],
  "targetFolderId": 0,
  "overwriteExisting": true
 }

Update the above Request body by:
- Replace X with the file ID (can also do a comma separated list of file IDs) you want to move to the new folder.  
- Replace 0 with the folder ID you want to move the file(s) into.  
- If you wish to overwrite a file (with the same name) in the destination folder then leave overwriteExisting set to true.  
- If you change overwriteExisting to false and it encounters a file in the destination folder with the same name, it will not move the file and will return a response of “File already exists.”

Download a file
~~~~~~~~~~~~~~~~~

To download a file from Shufflrr use the files download API.  Replace the {id} in the URL below with the ID of the file you want to download.

This is a :blue:`GET` method.

The files download API can be found at:

`https://wwwapi.shufflrr.com/api/files/{id}/download`__

.. __: https://wwwapi.shufflrr.com/api/files/{id}/download

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Download`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Download

Remove file
~~~~~~~~~~~~

To remove a file from Shufflrr, use the delete file API.  Replace the {id} in the above URL with the file ID to be removed.  

If you wish to remove the file immediately send in an empty request body.  If you wish to set an expiry date on the file instead, set the fields value in the request to the ID of the file (or a comma separated list of files) you want to set an expiry Date on and set the expiryDate value to the date you want Shufflrr to automatically expire the file(s) on.  

This is a :red:`DELETE` method

The delete files API can be found at:

`https://wwwapi.shufflrr.com/api/files/{id}`__

.. __: https://wwwapi.shufflrr.com/api/files/{id}

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Delete_0`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Files/Files_Delete_0

Sample Request Body
####################

To remove immediately
$$$$$$$$$$$$$$$$$$$$$$

::

 {}
 
To set expire date
$$$$$$$$$$$$$$$$$$$

::

 {
  "fileIds": [
    0
  ],
  "expiryDate": "2020-10-27T22:39:59.678Z",
  "clearExpiryDate": false
 }
 
Replace 0 with the ID of the file (or comma separated list of the files) you wish to set the expire date on.  Replace the value in the expiryDate element to contain the time and date you want Shufflrr to expire the file(s) on.


Presentation Slides
~~~~~~~~~~~~~~~~~~~~

To get information on all the slides of a specific presentation use the Presentation Slides API.  Replace the {id} in the url below with the file id of the presentation you want the slide information of.

This is a :blue:`GET` method.

The get file API can be found at:

`https://wwwapi.shufflrr.com/api/presentations/{id}/slides`__

.. __: https://wwwapi.shufflrr.com/api/presentations/{id}/slides

Documentation can be found at:

`https://wwwapi.shufflrr.com/api/docs/ui/index#!/Presentations/Presentations_Slides`__

.. __: https://wwwapi.shufflrr.com/api/docs/ui/index#!/Presentations/Presentations_Slides

