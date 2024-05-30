$(document).ready(function() {
    $.ajax({
        url: '/task/completion_percentage/',
        method: 'GET',
        success: function(data) {
            var percentage = data.completion_percentage;
            $('#progress-circle').css('--percentage', percentage);
            $('#progress-circle').attr('data-progress', percentage);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching completion percentage:", error);
        }
    });
});
