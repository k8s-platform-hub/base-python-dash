# base-python-dash

A simple python app using the dash framework. Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particuarly suited for anyone who works with data in Python.

# Deploy this project

```sh
$ hasura quickstart hasura/base-python-dash
$ cd base-python-dash
$ git add . && git commit -m "Initial Commit"
$ git push hasura master
```

Now, your app will be running at `https://dash.YOUR-CLUSTER-NAME.hasura-app.io` (replace `YOUR-CLUSTER-NAME` with the name of your cluster). To get the name of your cluster

```sh
$ hasura cluster status
```

Navigate to another page `https://dash.YOUR-CLUSTER-NAME.hasura-app.io/app1` to see different data graph. 

**Dash Base**

This app is a simple example of the capabilities of Dash developed by [Plotly](https://plot.ly/) and acts as an intro to overall Python framework.

Dash abstracts away all of the technologies and protocols required to build an interactive web-based application and is a simple and effective way to bind a user interface around
 your Python code.

To learn more check out Dash's [documentation](https://plot.ly/dash).

The following are screenshots for the app in this repo:
![Alt desc](https://github.com/hasura/base-python-dash/raw/master/microservices/dash/base-python-dash.png)
