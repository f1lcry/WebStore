window.onload = function() {
    $("input[type='number']").on("change", function() {
        let linkCurrent = event.target
        console.log(linkCurrent)
        $.ajax({
            url: "/cart/edit/" + linkCurrent.name + "/" + linkCurrent.value,
            data: {"name": linkCurrent.name},
            success: function(data) {
                $("#totalCart").html(data.result)
            }
        })
    });

    $(".remove").click(function() {
        let linkCurrent = event.target
        $.ajax({
            url: "/cart/remove/" + linkCurrent.value,
            success: function(data) {
                $("#totalCart").html(data.result)
                linkCurrent.parentElement.parentElement.remove()
            }
        })
        console.log(linkCurrent)
        console.log(linkCurrent.value)
    });

    $("input[type='checkbox']").on("change", function() {
        let linkCurrent = event.target

//        let data_attribute = $(this).data("cart-pk")
//        $(this).data("cart-pk")
//        let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val()
//
//        function csrfSafeMethod(method) {
//            // these HTTP methods do not require CSRF protection
//            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
//        }
//
//        $.ajaxSetup({
//            beforeSend: function (xhr, settings) {
//                // if not safe, set csrftoken
//                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
//                }
//            }
//        })

        // TODO(!): Узнать как можно изменить html у #totalCart элемента, а не у #innerProducts
        if ($(this).prop("checked")){
            $.ajax({
                url: "/cart/check/" + "1",
                data: {"cart_pk": $(this).data("cart-pk")},
                success: function(data) {
                    $("#totalCart").html(data.result)
//                    location.reload()
                }
            })
        }
        else {
            $.ajax({
                url: "/cart/check/" + "0",
                data: {"cart_pk": $(this).data("cart-pk")},
                success: function(data) {
                    $("#totalCart").html(data.result)
//                    location.reload()
                }
            })
        }
        console.log($(this).data("cart-pk"))
        console.log($(this).prop("checked"))
        console.log(linkCurrent.value)
    })
}
