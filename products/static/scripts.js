$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var nmb = $('#quantity').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);
        
            var data{};
            data.product_id = product_id;
            data.nmb = nmb;
             var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
             data["csrfmiddlewaretoken"] = csrf_token;
             var url = form.attr("action")
        
        $('.basket-items ul').append('<li>'+product_name+', ' + nmb + 'шт. ' + 'по ' + product_price + 'BYN ' + '<a class="delete-item" href=""></a>'+ '</li>');
    });

    function showingBasket() {
        $('.basket-items').removeClass('hidden');
    };

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseover(function () {
        showingBasket();
    });

    $('.basket-container').mouseout(function () {
        showingBasket();
    });

    // $(document).on('click', '.delete-item', function (e) {
    //     e.preventDefault();
    //     $(this).closest('li').remove();
    // })
});