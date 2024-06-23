

$(document).ready(function(){
    $(".filter-checkbox").on("click", function(){
        console.log("A checkbox have been clicked");
        
        let filter_object = {}

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")
            // console.log("Filter value is:", filter_value);
            // console.log("Filter key is:", filter_key);
            filter_object[filter_key] = 
Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(element){
                return element.value
            })   
        })
        console.log("Filter Object is: ", filter_object)
        $.ajax({
            url: 'filter-products/',
            data: filter_object,
            dataType: 'json', 
            beforeSend: function() {
                console.log("Trying to filter product...");
            },
            success: function(response){
                console.log(response)
                console.log("Data filtered successfully...");
                $("#filtered-product").html(response.data)
            }
        })
    })
})