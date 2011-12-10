Tasks = {
    load: function(){
        var task_template = _.template($("#task-template").html());
        $.getJSON('/tasks/', function(data){
            _(data.tasks).each(function(task){
                $("#task-list").append("<li>"+task_template(task)+"</li>")
            });
        })
    }
    ,complete: function(id, checked){
        $.ajax({
             url: '/tasks/'+id
            ,data: {complete: checked}
            ,type: "PUT"
            ,dataType: "json"
        });
    }
    ,create: function(content){
        var task_template = _.template($("#task-template").html());
        $.post('/tasks/', {content: content}, function(task){
            $("#task-list").prepend("<li>"+task_template(task)+"</li>")
        });
    }
    ,destroy: function(id){
        $.ajax({
             url: '/tasks/'+id
            ,type: "DELETE"
            ,success: function(){
                $("#task_"+id).closest("li").remove();
            }
        });
    }
    
};


$(function(){
    Tasks.load();

    //evento para cuando se cree una tarea:
    $("#task-input").keypress(function(e){
        var code = e.keyCode || e.which;
        var value;
        if (code == 13){
           value = $(this).val();
           $(this).val("");
           Tasks.create(value);
        }
    });


    //para cuando se quiera eliminar una tarea
    $(".delete-task").live('click', function(e){
        e.preventDefault();
        var id = $(this).data("id");
        Tasks.destroy(id);
    });
    
    $(".complete-task").live('click', function(e){
        Tasks.complete($(this).data('id'),$(this).is(":checked"));
    });
});
