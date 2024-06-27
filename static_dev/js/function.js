$(document).ready(function(){
    let filter_object = {}
    $("#sort").on("change", function(){
        var sortid = $("#sort").val();
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
        if (parseInt(filter_object.min_price) > parseInt(filter_object.max_price)){
            console.log("Default min price:", $("#min_price").attr("min"))
            console.log("Default max price:", $("#max_price").attr("max"))
            filter_object.min_price = parseInt($("#min_price").attr("min"))
            filter_object.max_price = parseInt($("#max_price").attr("max"))
        }
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

