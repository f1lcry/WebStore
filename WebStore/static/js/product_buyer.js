window.onload = function() {
    $("#addProductButton").click(function() {
        let linkCurrent = event.target
        $.ajax({
            url: '/cart/add/' + linkCurrent.value
//            success: function(data) {
//                console.log("ok")
//            }
        })
//        console.log(linkCurrent.value)
//        console.log(linkCurrent.id)
    })
}