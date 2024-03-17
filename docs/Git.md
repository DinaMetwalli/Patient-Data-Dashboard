# Git
Guide for working with repository and making contributions.

## Pulling Changes
Always make sure to pull the latest changes before you start working. This is done on the main branch only and can be done using the `git pull` command. if the branch you're working on is yours then there is no need for git pull.

## Branches
When creating a new feature (e.g. you're assigned to work on the Patient class and you will start implementing it now), make sure to create a new branch for that feature. Two people can't work on the same branch, meaning this will be your branch.

To create a new branch, use `git checkout -b <branchname>` and replace the <> with the name of your branch.
When switching to a branch that already exists, use `git checkout <branchname>`.

You can check the branch you're currently on using `git branch`.

## Committing
Committing your changes to the code is done using `git commit`. When you type this command on vscode, a new file will open up temporarily for you to type in the commit message. After typing the message you can save the file and close it using `Ctrl + W` and then pressing save. This will commit your changes.

You should follow [Conventional Commits](https://www.conventionalcommits.org) for your commit messages. This will add consistency and clarity, allowing for easier navigation of changes as well as version control. The following shows the main commit types:

- `feat` - A new feature
- `fix` - A bug fix
- `docs` - Documentation only changes
- `style` - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor` - A code change that neither fixes a bug nor adds a feature
- `perf` - A code change that improves performance
- `test` - Adding missing tests or correcting existing tests
- `chore` - Changes to the build process or auxiliary tools and libraries such as documentation generation
- `ci` - Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)

An example of a convetional commit could be `feat(gui): add importing csv page`. `feat` indicates the type of the commit, a new feature. `(gui)` indicates the scope of the commit, in this case you're working on the GUI. and after the colon is the commit message. The scope of the commit is optional, you could choose not to add it if you don't think the commit falls under a specific scope.

`Note: Please make sure to commit every time you make a change, don't write 1000 lines of code and commit all of it in one go, it only makes things very confusing. (Serhii this is directed at you)`

## Pushing
You should push your changes to the remote repository so others can see and pull them as well. You do this using `git push`. If you're pushing changes from a new branch for the first time, this will be `git push --set-upstream origin <branchname>`. After that inital push you can simply use `git push`.

## Pull Requests
When you're finished implementing your feature, you can create a pull request to merge it with the main branch. `NO COMMITS SHOULD BE MADE DIRECTLY TO THE MAIN BRANCH! (Serhii, once again this is for you).` After you push your changes you will find an option on the repository's site to create a pull request. In order to merge your request a code review by another team member is needed first. You could also assign other members to review your code. However, you can't merge your changes to the main branch unless they've been reviewed.

## Merge Conflicts
As long as you follow all the rules specified in this guide, hopefully no merge conflicts should occur. However, if a merge conflict happens it is easy to fix, no need to worry `(cough cough)`.