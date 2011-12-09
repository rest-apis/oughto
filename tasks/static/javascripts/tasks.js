Tasks = {
    load: function(){
        var task_template = _.template($("#task-template").html());
        $.getJSON('/tasks/', function(data){
            _(data.tasks).each(function(task){
                $("#task-list").append("<li>"+task_template(task)+"</li>")
            });
        })
    }
};


$(function(){
    Tasks.load();
});
