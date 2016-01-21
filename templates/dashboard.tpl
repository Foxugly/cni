{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block content %}
<div class='row row_space'>
    <div class="col-xs-12 text-center h1">Dashboard</div>
</div>
<div class='row'>
    <div class="col-xs-6">
        <div class="panel panel-primary">
            <div class="panel-heading">Planning</div>
            <div class="panel-body">
                <div class="panel-group">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse1">9:00 Renaud Vilain</a></h3>
                        </div>
                        <div id="collapse1" class="panel-collapse collapse">
                            <div class="panel-body">body renaud
                            </div>
                        </div>
                    </div>
                    <div class="panel panel-info">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse2">9:30 Claire Gheurs</a></h3>
                        </div>
                        <div id="collapse2" class="panel-collapse collapse">
                            <div class="panel-body">body kiki
                            </div>
                        </div>
                    </div>
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title"><a data-toggle="collapse" href="#collapse3">10:00 Alyssia Ferrarese</a></h3>
                        </div>
                        <div id="collapse3" class="panel-collapse collapse">
                            <div class="panel-body">body Alyssia
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xs-6">
        <div class="panel panel-primary">
            <div class="panel-heading">
                {%  trans "Orders of business" %}
                <span class="pull-right">
                    <button type="button" class="btn btn-xs btn-primary" title="list">
                        <span class="glyphicon glyphicon-list"></span>
                    </button>
                </span>
            </div>
            <div class="panel-body">
                <ul class="list-group">
                {%  for oob in user.userprofile.current_club.orders_of_business.all %}
                <li class="list-group-item"><a href="{%  url 'oob_view' oob.id %}">{{ oob }}</a>
                    <span class="pull-right">
                        <button type="button" class="btn btn-xs btn-info"  title="pdf" >
                            <span class="glyphicon glyphicon-file"></span>
                        </button>
                        <button type="button" class="btn btn-xs btn-success" title="create report">
                            <span class="glyphicon glyphicon-duplicate"></span>
                        </button>
                        <button type="button" class="btn btn-xs btn-warning" title="send">
                            <span class="glyphicon glyphicon-envelope"></span>
                        </button>
                        <button type="button" class="btn btn-xs btn-danger" title="remove">
                            <span class="glyphicon glyphicon-remove"></span>
                        </button>
                    </span>
                </li>
                {%  endfor %}
                </ul>
                <div class="text-center">
                    <a href="{% url 'oob_add' %}" class="btn btn-success"><span class="glyphicon glyphicon-plus"></span> Add Order of business</a>
                </div>
            </div>
        </div>
        <div class="panel panel-primary">
            <div class="panel-heading">
                {%  trans "Reports" %}
                <span class="pull-right">
                    <button type="button" class="btn btn-xs btn-primary" title="list">
                        <span class="glyphicon glyphicon-list"></span>
                    </button>
                </span>
            </div>
            <div class="panel-body">
                <div class="text-center">You scheduled slots to 20/02/2016 (15 days)</div>
                <div class="text-center row_space_top"><a href="/user/model/" class="btn btn-default"><span class="glyphicon glyphicon-equalizer"></span> {% blocktrans %} Model{% endblocktrans %}</a></div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
