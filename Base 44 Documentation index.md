> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with branches

> Create branches to try new ideas, features, or redesigns without affecting your app, work on several in parallel, then merge each one into main when ready.

Branches let you try new ideas, features, or redesigns without affecting your app. Each branch has its own chat and its own live preview, and you can **work on several branches in parallel**, then merge each one into your app when you are happy with the result.

<Frame caption="Work on several branches alongside your main app">
  <img src="https://mintcdn.com/base44/eYkTlSr5OX-PNhnp/images/Branches-hero.png?fit=max&auto=format&n=eYkTlSr5OX-PNhnp&q=85&s=1bb140d0e46f3e392dfabc8d8b0cd77a" alt="The branch menu listing several branches next to an app preview" width="1200" height="660" data-path="images/Branches-hero.png" />
</Frame>

<Card title="Ways to use a branch" icon="code-branch">
  * **Test a redesign.** Try a new look for your app and compare it with the current version. If you change your mind, leave the branch behind.
  * **Keep your live app ready.** When a small fix comes up mid-project, fix and publish it from main right away. Your bigger work in progress stays safely on its branch.
  * **Build a feature that launches later.** Work ahead of a release and keep the feature on a branch until launch day.
  * **Work in parallel.** Build on several branches at the same time, and work with your team on different ideas at once, each on their own branch.
</Card>

<Note>
  Branches work alongside a [GitHub](/developers/app-code/local-development/github) connection. Base44 keeps each branch as a real branch in your repository, and you can also [build on a branch that is already there](#importing-a-branch-from-github).
</Note>

***

## How branches work

Your app's main version is called **main**. When you create a branch, Base44 starts a separate line of work from the current state of main.

Each branch keeps its own chat, live preview, and copy of your app's design and pages, so changes you make stay on the branch until you merge them. A branch also builds on its own and keeps its own version history, so branches run in parallel and you can return to any earlier point without touching main.

Some things stay shared across main and every branch. Your app's data is the same live records everywhere, and record changes happen on main. Your connections and automation, including integrations, secrets, automations, workflows, and in-app agents, are shared too, along with your app's settings, domains, and published version.

<Warning>
  **A branch uses your real, live data.**

  * Records you add, change, or delete while previewing a branch affect the same data your app uses everywhere.
  * To experiment without touching your live data, switch your preview to test data while you work. Test data is available on the [Builder plan](https://base44.com/pricing) and higher. Learn more about [testing your app with test data](/documentation/managing-app-data/testing-your-data).
</Warning>

***

## Creating a branch

Describe what you want to build, and Base44 creates the branch, names it from your first message, and starts building right away. Branch names are short, 3 words or fewer, and always in English, whatever language you write in. The name is set automatically, and a branch cannot be renamed.

<Tip>
  **Before you begin:** If your app was built a while ago, you may need to make one change on main before you can create your first branch. If that applies to your app, Base44 tells you when you try.
</Tip>

**To create a branch:**

1. In the app editor, click your app's logo or name at the top of the chat panel.
2. Click **Create new branch**.
3. Pick one of the suggestions, or type what you want to build in the chat box.
4. Send the message.

<Frame caption="Creating your first branch from the branch menu">
  <img className="mx-auto" style={{ width:"55%" }} alt="The branch menu open under the app name, showing Main chat and a Create your first branch panel with the Create new branch button highlighted" src="https://mintcdn.com/base44/-o0DdlVp5o4iVuNu/images/create-new-branch.png?fit=max&auto=format&n=-o0DdlVp5o4iVuNu&q=85&s=69471911ab96daf19dc80f2c353f4dd5" width="1474" height="694" data-path="images/create-new-branch.png" />
</Frame>

<Note>
  Branches always start from main. If you create a branch while you are on another branch, the new branch still starts from main.
</Note>

Branches work on your phone as well, both in a mobile browser and in the Base44 app. The branch menu appears at the top of the editor as soon as your app has a branch, so create your first branch from a desktop browser, then switch between branches, build, and merge from your phone.

***

## Importing a branch from GitHub

When your app is connected to GitHub, you can build on a branch that already exists in your repository. Base44 works on that branch itself, so your changes and Base44's go to the same branch in your repository.

**To import a branch from GitHub:**

1. In the app editor, click your app's logo or name at the top of the chat panel.
2. Click **Import from GitHub**.
3. Search for the branch you want, then select it.
4. Click **Import**.

<Note>
  You import from the repository your app is connected to. A branch you create in Base44 gets a new branch in that same repository.
</Note>

***

## Working on a branch

While you are on a branch, the branch's name replaces your app's name at the top of the chat panel, and a spinning icon shows when the AI is working. You build on a branch the same way you build on main: describe what you want in the chat. Selecting an element and making a visual edit saves to the branch you are on too, the same as your chat changes.

A few things work differently on a branch:

* **Merge to main** replaces the **Publish** button. You publish changes from main after merging.
* The preview shows the branch's version of your app.
* The page URL includes the branch, so you can share a link that opens the app editor on that branch.

<Tip>
  **Branches run in parallel.** Send a request on one branch, switch to another, and keep building there while the first one finishes. Your app runs up to 5 builds at the same time, so you and your team can move on several ideas at once, each on their own branch.

  The branch menu shows which branches are building, so you can check on them as you go.
</Tip>

### Actions that happen on main

You do most of your building on a branch, but some actions affect your whole app, not just one branch. Those always happen on main, even while you are working on a branch:

* Publishing your app
* Creating or changing secrets, connectors, automations, workflows, and in-app agents
* Changing your app's theme settings
* Undoing a message in the chat, or editing and resending one
* Adding a page from Figma
* Asking the AI to add, change, delete, or import records

<Note>
  If you ask for one of these on a branch, Base44 asks you to do it on main or merge the branch first.
</Note>

### Entities on a branch

You can create entities and add fields to entities you already have on a branch, and both are live in that branch's own preview right away. On an entity you create, you set everything, including its [data permissions](/Setting-up-your-app/Managing-security-settings). On an entity that already exists, additions apply, so keep a new field optional, because your existing records do not have it yet.

Removing an entity or a field, changing an existing field's type or whether it is required, and changing data permissions happen on main. Make the change there and your branch picks it up right away, with no merge or update needed.

Records are your app's live data, shared with main, so ask the AI for record changes on main rather than on a branch. Adding, changing, or deleting records yourself while previewing a branch works as it always does, and it changes the same data your app uses everywhere.

### Backend functions on a branch

You can add and change backend functions on a branch. The branch gets its own copy of each function you touch, along with the shared files those functions import, so you can update a helper and the function that uses it together. The branch preview calls the branch's version, and merging the branch deploys it to main. Your app's first backend function is created on main, and you can work on functions from a branch after that. On an app imported from GitHub, backend changes stay on main.

### Code on a branch

The **Code** tab shows your app's files as they are on the branch you are on, rather than as they are on main. You can edit them there, and what you save stays in the branch until you merge it.

<Frame caption="The Code tab on a branch, showing that branch's own files">
  <img src="https://mintcdn.com/base44/Fe1EUhgmdxe2q9Xg/images/code-branch.png?fit=max&auto=format&n=Fe1EUhgmdxe2q9Xg&q=85&s=ff4e8356471462b17c55feae3bdda51b" alt="The Code tab open on a branch, with the branch's file tree and Merge to main at the top right" width="1924" height="1174" data-path="images/code-branch.png" />
</Frame>

The files behind your app's pages, layout, and styling save straight to the branch, so you can try a code change and leave main untouched. Backend function files save to the branch too. See [backend functions on a branch](#backend-functions-on-a-branch) for when a change is live in the branch's preview and when it waits for the merge.

You do not need to keep track of which is which. A few files change your whole app rather than one branch, and Base44 stops the save and tells you where to go instead:

* **Entity files:** Ask for the change in the branch's chat, or switch to main. See [entities on a branch](#entities-on-a-branch) for what a branch can change on its own.
* **Anything that would change your live app:** Make the change on main, and your branch picks it up with no merge needed.

<Note>
  Redeploying a backend function replaces the one your live app runs, so it happens on main.
</Note>

***

## Using version history on a branch

Every version saved on a branch is listed in that branch's own version history, so you can look back at how the branch developed and return to any earlier point. Restoring a version changes that branch only, and main stays exactly as it is. A merged branch keeps its version history readable, and you can restore while a branch is still active.

**To restore an earlier version of a branch:**

1. On the branch, click the **Version history** icon at the top of the chat panel.
2. Click a version in the list to load it in the preview.
3. Click the **More options** icon <Icon icon="ellipsis" /> next to that version.
4. Click **Revert to this version**.

Restoring brings the branch's pages, design, entities, and backend functions back to that version, and the branch's chat returns to the message that created it. Your records are shared with main, so they stay as they are. Your later versions stay in the list, so you can move forward again whenever you want.

<Note>
  **Restoring and publishing from a branch:**

  * **Publish this version** is available on main only, because publishing always ships your main app. To release work from a branch, merge it into main and publish from there.
  * Restore a version once the branch has finished building and any update from main is complete. If the branch is busy, Base44 tells you so, and you can restore as soon as it finishes.
</Note>

***

## Switching between branches

You can move between main and your branches at any time, and every branch keeps its changes until you merge it. On a branch, you can also click the **X** next to **Merge to main** to exit back to main.

**To switch to another branch or back to main:**

1. Click the branch name at the top of the chat panel.
2. Select a branch from the list, or select **Main chat** to return to main.

<Frame caption="Switching between main and your branches">
  <img className="mx-auto" style={{ width:"55%" }} alt="The branch menu open on a branch, showing Main chat above the list of branches" src="https://mintcdn.com/base44/TEODQUOeOLz9wLnr/images/switching-branches.png?fit=max&auto=format&n=TEODQUOeOLz9wLnr&q=85&s=65c7341c40def5c857bf1a5927437e4b" width="692" height="868" data-path="images/switching-branches.png" />
</Frame>

The icon next to each branch shows its current status. Hover over the icon to see the label:

| Status      | Meaning                                                                        |
| ----------- | ------------------------------------------------------------------------------ |
| **Active**  | The branch is open and ready to build on.                                      |
| **Working** | The AI is building on this branch right now.                                   |
| **Merging** | The branch is being merged into main.                                          |
| **Merged**  | The branch was merged into main. Its chat stays readable, but it is read-only. |

<Note>
  You can switch branches while the AI is building, and it keeps working on the branch you left. Save or discard any edits on main first.
</Note>

***

## Updating a branch with changes from main

If main changes while your branch is open, a card appears above the chat box on the branch. It tells you how much changed on main and whether any of it overlaps with your branch.

When you update, the AI combines main's changes with your branch. If some changes overlap, the AI resolves them for you. If the two versions genuinely conflict, the AI asks you a question in the chat so you can decide what to keep.

**To bring main's latest changes into your branch:**

1. On the branch, find the update card above the chat box.
2. Click **Update branch**.

<Frame caption="The update card that appears above the chat box when main has changed">
  <img className="mx-auto" style={{ width:"55%" }} alt="An update card above the chat box reading 1 new message on main, Nothing overlaps, Ready to update, with an Update branch button" src="https://mintcdn.com/base44/-o0DdlVp5o4iVuNu/images/update-branch.png?fit=max&auto=format&n=-o0DdlVp5o4iVuNu&q=85&s=d822e374865edacdd62a793fc8c1452d" width="1600" height="1596" data-path="images/update-branch.png" />
</Frame>

You can also start an update from the branch menu. Click the **More actions** icon <Icon icon="ellipsis" /> next to a branch, then click **Update from main**.

<Note>
  If an update runs into a problem, Base44 rolls it back and your branch's work stays unchanged.
</Note>

***

## Merging a branch into main

Merging brings everything you built on the branch into main. Your changes reach your app's users only when you publish from main, so you decide exactly what goes out and when.

After the merge, a summary of the branch's changes appears in main's chat, and the branch stays in your branch list as merged, so you can still read its chat history, but it becomes read-only.

**To merge a branch:**

1. On the branch, click **Merge to main** at the top of the editor.
2. Review the confirmation, then click **Merge to main**.

<Frame caption="Click Merge to main at the top of the editor, then publish from main when you are ready">
  <img src="https://mintcdn.com/base44/-o0DdlVp5o4iVuNu/images/merge-to-main-publish.png?fit=max&auto=format&n=-o0DdlVp5o4iVuNu&q=85&s=ba59d7127384c7474246adc7b64f7927" alt="The app editor on a branch with the Merge to main button highlighted in the top bar" width="2924" height="994" data-path="images/merge-to-main-publish.png" />
</Frame>

<Tip>
  You can also ask the AI chat to merge or update a branch. It adds a one-click card to the chat that runs the action for you.
</Tip>

You can also merge from the branch menu. Click the **More actions** icon <Icon icon="ellipsis" /> next to a branch, then click **Merge to main**.

<Note>
  If the branch conflicts with changes made on main, Base44 asks you to update it first. [Update the branch from main](#updating-a-branch-with-changes-from-main) to resolve the conflicts, then merge again.
</Note>

***

## Deleting a branch

Delete a branch when you are done with an idea and want to clear it from your list. Your app and your other branches stay as they are.

<Warning>
  Deleting a branch is permanent. It removes the branch and its chat, and this cannot be undone. To keep the work, merge the branch into main first.
</Warning>

**To delete a branch:**

1. Click the branch name at the top of the chat panel.
2. Click the **More actions** icon <Icon icon="ellipsis" /> next to the branch you want to delete.
3. Click **Delete**.
4. Review the confirmation, then click **Delete branch**.

<Frame caption="Opening the More actions menu on a branch">
  <img className="mx-auto" style={{ width:"58%" }} alt="The branch menu with the More actions menu open on a branch, showing Merge to main, Update from main, and Delete" src="https://mintcdn.com/base44/aGvTNx4rVci6s1Hq/images/more-actions-branches.png?fit=max&auto=format&n=aGvTNx4rVci6s1Hq&q=85&s=5992199dcd0afd42dde4af7fc1b67f67" width="744" height="978" data-path="images/more-actions-branches.png" />
</Frame>

<Note>
  You can delete a branch once the AI finishes building on it and any update from main is complete. Merged branches stay in your list as a record of the work.
</Note>

***

## FAQs

Click a question below to learn more about branches.

<AccordionGroup>
  <Accordion title="Can I publish my app from a branch?">
    No. Publishing always happens from main. On a branch, the **Publish** button is replaced by **Merge to main**. Merge the branch first, then publish from main.
  </Accordion>

  <Accordion title="How many branches can I have?">
    There is no set limit. You can keep as many branches going at once as you want, and merge each one whenever it is ready.
  </Accordion>

  <Accordion title="Can my team and I work on different branches at the same time?">
    Yes. Each collaborator can open a different branch and chat there, and each branch builds on its own. Your app runs up to 5 builds at the same time, and anything beyond that waits in the queue and runs in order.

    Creating a branch needs edit access to the app, so members with the **Viewer** role can open branches and read their chats. Learn more about [roles in your workspace](/Account-and-billing/Managing-your-workspaces).
  </Accordion>

  <Accordion title="Do branches use extra credits?">
    No. Building on a branch uses credits the same way as building on main, from the same credit balance.
  </Accordion>

  <Accordion title="Can I use branches on an app connected to GitHub?">
    Yes. Create a branch the way you would on any app, and Base44 adds the matching branch to your connected [GitHub](/developers/app-code/local-development/github) repository. To build on a branch that is already in your repository, use [Import from GitHub](#importing-a-branch-from-github).
  </Accordion>

  <Accordion title="Can I connect my app to GitHub while I have branches?">
    Yes. Base44 adds your open branches to the repository when you connect, so there is nothing to merge or delete first. If a branch is building at that moment, wait for it to finish, then connect.
  </Accordion>

  <Accordion title="Can I use branches on an app I migrated into Base44?">
    Yes. An app you [migrated from another platform](/Getting-Started/migrating-an-existing-app) works with branches from the same branch menu as any other Base44 app.
  </Accordion>
</AccordionGroup>
