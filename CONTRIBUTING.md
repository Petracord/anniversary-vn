This page gives a brief outline of how you can contribute to this project. For any questions and suggestions, feel free to leave comments, open issues or join the Discord server and apply for the project role.

## 1. Setup

First, if you've not done so already, [install git](https://git-scm.com/), the repository management system we're using for development on this project. We will go over the general workflow for the project in a later section. If you don't feel like dealing with command line software, feel free to download any of the many git GUI clients (such as [GitHub Desktop](https://desktop.github.com/)).  
You also need to create a account on this service, [GitLab](gitlab.com), to contribute.  

This project is developed in Ren'py, a free open-source engine for developing visual novel style games. Thus, you of course need to [download and install this software](https://www.renpy.org/) to proceed. The version shouldn't matter too much, but pick the latest 7.x.x version for the sake of consistency.  
You may also need a text editor to work with Ren'py. Since the previous go-to choice of Atom has been discontinued, you can use [Visual Studio Code](https://code.visualstudio.com/download) as an alternative. After installing the editor, make sure to [also install the Ren'Py language support extension](https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy).

Finally, in order to contribute you will need to *fork* the project to your own GitLab account. Navigate to the [project page](https://gitlab.com/petracord-productions/1st-anniversary-vn) and in the top right corner click the "Forks" and then "Fork project" on the page you've been redirected to. After waiting for the operation to be processed, you'll find yourself on your very own version of the project.  
Click on "Clone" and copy the URL (or the SSH URI if you've [set up your GitLab account with an SSL key]). Finally, open a command line and type `git clone [CLONE_URL]` or paste the URL into your Git GUI of choice. The project fork should now be downloaded to your local system.
To verify that everything worked, open Ren'py and check where your project folder is located by checking `Settings > Project Directory`. Either set this to the parent directory of your freshly cloned repository or move the entire repository into this folder. Now, after hitting "Refresh", the cloned project should be visible in the selection. Click it, then click "Launch Project" to see if everything works (there shouldn't be a runtime error if you're on the "master" branch).
If everything works, you're done with the setup.

## 2. Contributing

We can now get strated contributing to the project. This section will explain how to find tasks and how to get your changes accepted in the main project.

### 2.1 What do I work on?

There are two pages that are mainly interesting for finding tasks to work on:

* [Milestones](https://gitlab.com/petracord-productions/1st-anniversary-vn/-/milestones) contain larger, overarching goals we're working towards. Check here first to see if there are any pressing tasks in the works
* [Issues](https://gitlab.com/petracord-productions/1st-anniversary-vn/-/issues) are concrete things to be worked on, such as implementations and bugs. Milestones will consist of several issues

You can also ask around in the project channels of the Discord.
