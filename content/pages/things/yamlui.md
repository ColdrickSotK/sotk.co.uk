Title: yamlui
Slug: yamlui
URL: things/yamlui/
Save_as: things/yamlui/index.html
Thing: yes
Type: software
Links: See the code;https://github.com/ColdrickSotK/yamlui
Summary: yamlui is an extensible set of declarative UI widgets for use with pygame. It allows (fairly) simple creation of UI layouts by editing YAML files, rather than hardcoding everything.

`yamlui` is a Python library which provides a number of UI widgets
for pygame. It also allows interfaces made of these widgets to be
defined in YAML files rather than in code, reducing the amount of
time that needs to be spent writing UI boilerplate and allowing
focus on the functionality behind the UI.

## Extensibility

In addition to providing a basic set of widgets including textboxes,
containers, buttons, and labels, `yamlui` is easy to extend with
your own custom widgets. These can be based on existing widgets by
subclassing them, or entirely custom so long as they provide the
same API. The extensibility is done simply by adding to a dictionary
before calling the UI generation function.

    :::python
    yamlui.class_mapping.update({
        'viewport': MyViewport
    })

This example adds a `viewport` widget which is represented by the
`MyViewport` class.

## Callbacks

The defined UI can be dynamically changed and respond to user input
through the use of various callbacks and data bindings. For example,
a label can define `content-bind`, which will cause the content of
the label to be the result of calling the specified function.

```
:::yaml
- object: label
  style: ['label']
  properties:
    name: starting-villagers
    text: '0'
    width: 25
    position: [170, 180]
    content-bind: villager_count
```

And the accompanying code,

    :::python
    def villager_count(event=None, widget=None, **kwargs):
        return str(len(villagers))

    yamlui.callbacks.update({
      'villager_count': villager_count
    })

As with adding new widgets, this needs to be done before actually
generating the UI.
