(function($) {
    function csrf_token(obj) {
        var key = 'csrfmiddlewaretoken';
        var value = $('input[name="' + key + '"]').val();
        obj[key] = value;
        return obj;
    }

    $(document).ready(function() {
        $('#fighters-filter-quality').change(function() {
            var endpoint = $(this).data('endpoint');
            var quality  = $(this).val();
            $.ajax({
                url: endpoint,
                dataType: 'json',
                method: 'GET',
                data: csrf_token({ajax: true, quality: quality}),
                success: function(result) {
                    if (result.data.html) {
                        $('#list_fighters').quicksand($(result.data.html));
                    }
                },
                error: function() {
                    alert('Error');
                }
            });
        });
    });
})(jQuery);