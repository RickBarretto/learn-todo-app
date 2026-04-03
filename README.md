# Simple TODO

This repository aims to learn new technologies, libraries, frameworks,
architectures, etc, etc. for a simple TODO app application.

The idea is being the basic enough to implement this into one hour
of work without AI assistance.

## Description

A single-page app where users can:

- Add a to-do item
- Mark it as done
- Delete a to-do
- Filter between all/active/completed items

## Basic Features

```feature
Feature: Add a new to-do

Scenario: User adds a new to-do item
  Given the user is on the home page
  When the user types “Buy groceries” into the input field and presses enter
  Then a new to-do item with text “Buy groceries” should appear in the list
    And the item should be marked as not done
```

```feature
Feature: Mark a to-do as completed

Scenario: User marks a to-do as completed
  Given a to-do item “Buy groceries” exists in the list
  When the user clicks the checkbox next to the item
  Then the item should be visually marked as completed
    And its state should be saved as completed
```

```feature
Feature: Delete a to-do

Scenario: User deletes a to-do item
  Given a to-do item “Buy groceries” exists in the list
  When the user clicks the delete button on that item
  Then the item should be removed from the list
```

```feature
Feature: Filter to-dos

Scenario: User filters to show only active items
  Given there are multiple to-do items with varying completion status
  When the user clicks the “Active” filter button
  Then only the items that are not completed should be visible
```

```feature
Scenario: User filters to show only completed items
  Given there are multiple to-do items with varying completion status
  When the user clicks the “Completed” filter button
  Then only the items that are completed should be visible
```


## Advanced Features

```
Feature: User registration

Scenario: User registers with valid email
  Given the user is on the registration page
  When the user enters rick@example.com and submits the form
  Then a verification email should be “sent”
    And the user sees a message “Please verify your email to continue”

Scenario: User registers with invalid email
  Given the user is on the registration page
  When the user enters rick@.com and submits the form
  Then the user should see an error message “Invalid email format”
```


```
Feature: Email verification

Scenario: User verifies email
  Given the user has registered with rick@example.com
    And the email is not verified
  When the user clicks the verification link or button
  Then the user account should be marked as verified
    And the user can now add to-do items


Scenario: Unverified user tries to add to-do
  Given the user is logged in but email is not verified
  When the user tries to add a to-do item
  Then the user should see a message “Verify your email first”
```

```
Feature: Add a new to-do (verified users only)

Scenario: Verified user adds a new to-do
  Given the user is logged in and verified
  When the user types “Buy groceries” and presses enter
  Then the to-do appears in the list marked as not done
```
