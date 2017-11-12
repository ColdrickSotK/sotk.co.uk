Title: StoryBoard
Slug: storyboard
URL: things/storyboard/
Save_as: things/storyboard/index.html
Thing: yes
Type: software
Links: See the code;http://git.openstack.org/cgit/openstack-infra/storyboard/
       See a demo;https://storyboard-dev.openstack.org/
Summary: StoryBoard is a tool to track tasks and issues in interrelated projects. It is currently used by a number of teams in the OpenStack project.

StoryBoard is a tool for tracking issues and tasks across multiple
interrelated projects. It started out as an OpenStack Infrastructure
project, and is currently used by a number of teams in the wider
OpenStack project.

## Overview

StoryBoard was designed to facilitate cross-project work in large
communities like OpenStack. It contains a number of concepts familiar
from other tools, with as many points of contention removed so as to
ease collaboration between separate teams.

The most simple thing in StoryBoard is a single **task**. A task
describes a single piece of work for a particular **project**. If the
work involves writing code, then a task should map to a single commit.
All tasks are part of a **story**. A story is a description of a
feature or issue, and the tasks in a story represent the work needed
in order to implement the feature or fix the issue. A story can have
multiple tasks for multiple projects, allowing work of any size across
any number of projects to be tracked in a single place.

## Priority

In most task/issue trackers each item (for example a task) is given a
single priority, which is set by either someone who claims
responsibilty for the task, or management after discussions
or prioritization meetings. This approach doesn't scale for situations
where multiple distinct stakeholders may have equally valid and utterly
different opinions on priority.

As an example, the lead of an open source project and the manager who
is paying you to work on something in that project for your company
may have conflicting opinions on what the priorities for the project
should be, and obviously the project's work tracker will reflect the
project lead's opinions.

In StoryBoard there is no global priority field for tasks. Instead,
tasks can be added to **worklists**, which can be ordered however their
users' see fit. This allows a person or group of people to assert the
priority of a task to them by adding it to a worklist named "Alice's
priorities", or "StoryBoard Team High Priority" for example.

Other folk can **subscribe** to these worklists if they care about
those people's opinions on priority, and then see which of the
worklists they're subscribed to contain a task when they are exploring
stories and tasks.

This allows everyone's opinion of priorities to be tracked in the same
place, and makes it easy to care about the opinion of multiple folk.

## Workflow

StoryBoard also provides a concept of **boards**, which are a flexible
idea that can be used to track work using a kanban workflow, or used
to further refine the idea of complex priority, or other things for
which the ability to arrange tasks or stories into arbitrary lanes is
useful.
