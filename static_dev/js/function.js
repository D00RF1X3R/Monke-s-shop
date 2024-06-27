$(document).ready(function(){
    let filter_object = {}
    $("#populate-low").on("click", function(){
        var sortid = 'populate-low';
        filter_object["sortid"] = sortid;
        console.log("Sort-id is:", sortid);
        console.log("Filter Object is: ", filter_object);
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
    $("#populate-high").on("click", function(){
        var sortid = 'populate-high';
        filter_object["sortid"] = sortid;
        console.log("Sort-id is:", sortid);
        console.log("Filter Object is: ", filter_object);
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
    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        console.log("A checkbox have been clicked");
        $("#max_price").each(function(){
            let max_price = $(this).val()
            filter_object.max_price = max_price
            console.log("Max price is:", max_price);
        })
        $("#min_price").each(function(){
            let min_price = $(this).val()
            filter_object.min_price = min_price
            console.log("Min price is:", min_price);
        })
        $(".filter-checkbox").each(function(){
            
            let filter_key = $(this).data("filter")
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

