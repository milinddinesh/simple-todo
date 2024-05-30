$(document).ready(function() {
    $.ajax({
        url: '/task/completion_percentage/',
        method: 'GET',
        success: function(data) {
            var percentage = data.completion_percentage;
            $('.progress').attr('data-value', percentage);
            updateProgressBar(percentage);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching completion percentage:", error);
        }
    });

    function updateProgressBar(value) {
        var left = $('.progress-left .progress-bar');
        var right = $('.progress-right .progress-bar');

        if (value > 0) {
            if (value <= 50) {
                right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)');
            } else {
                right.css('transform', 'rotate(180deg)');
                left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)');
            }
        }

        $('.progress-value .h2').text(value + '%');
    }

    function percentageToDegrees(percentage) {
        return percentage / 100 * 360;
    }
});
