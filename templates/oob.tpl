{% extends "layout.tpl" %}
{% load bootstrap3 %}
{% load i18n %}
{% load staticfiles %}

{% block js %}
<script>
function rm_subject(self){
    $(self).parent().parent().remove();
}
$(document).ready(function() {
    $('#add_subject').click(function () {
        $('#subjects').append('<div class="input-group"><input name="subject[]" type="text" class="form-control" placeholder="Subject"><span class="input-group-btn"> <button type="button" class="btn btn-danger" onclick="rm_subject(this);"><span class="glyphicon glyphicon-remove"></span></button></span> </div>');
    });
});
</script>
{% endblock %}

{% block content %}
    <div class="row row_space" >
        <div class="col-md-12 text-center"><h1>{{title}}</h1></div>
    </div>
<form class="form-horizontal" method="post" action="{{url}}" {% if enctype_form %} {{enctype_form|safe}} {% endif %} >
  {% csrf_token %}
    <div class="row">
        {% for f in form %}
            {% bootstrap_form f layout="horizontal"%}
        {%  endfor %}
    </div>
    <div class="row">
        <div class="form-group">
            <label class="col-md-3 control-label" for="id_subjets">Subjects</label>
            <div id=subjects class="col-md-9">
                {% if instance %}
                    {% for subject in instance.subjects.all %}
                        <div class="input-group">
                            <input name="subject[]" type="text" class="form-control" placeholder="Subject" value="{{ subject.subject }}">
                            <span class="input-group-btn">
                                <button type="button" class="btn btn-danger" onclick="rm_subject(this);"><span class="glyphicon glyphicon-remove"></span></button>
                            </span>
                        </div>
                    {%  empty %}
                        <div class="input-group">
                            <input name="subject[]" type="text" class="form-control" placeholder="Subject">
                            <span class="input-group-btn">
                                <button type="button" class="btn btn-danger" onclick="rm_subject(this);"><span class="glyphicon glyphicon-remove"></span></button>
                            </span>
                        </div>
                    {%  endfor %}
                {%  else %}
                <div class="input-group">
                    <input name="subject[]" type="text" class="form-control" placeholder="Subject">
                    <span class="input-group-btn">
                        <button type="button" class="btn btn-danger" onclick="rm_subject(this);"><span class="glyphicon glyphicon-remove"></span></button>
                    </span>
                </div>
                {%  endif  %}
            </div>
        </div>
    </div>
    <div class="row">
      <div class="form_group">
        <div class="col-md-9 col-md-offset-3">
          <button type="submit" class="btn btn-primary"> {%  trans "Submit" %}</button> <a href="#" id="add_subject" class="btn btn-success"><span class="glyphicon glyphicon-plus"></span> Add Subject</a>
            {% if instance %}
               <a href="#" id="add_subject" class="btn btn-warning"><span class="glyphicon glyphicon-envelope"></span> Send to the board of directors</a>
               <a href="#" id="add_subject" class="btn btn-danger"><span class="glyphicon glyphicon-remove"></span> Remove </a>
            {% endif %}
        </div>
      </div>
    </div>
</form>
{% endblock %}
