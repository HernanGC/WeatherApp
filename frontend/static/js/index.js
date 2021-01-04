$('document').ready(function () {

var csrf = $('input[name=csrfmiddlewaretoken]').val();


const kelvinToCelsius = function (temp) {
    return Math.round(Number(temp) - 273.15 * 10 / 10) 
}

$('#search-form').submit(function (e) {
    e.preventDefault();
    if ($('.form-control').val()) {
        let myData = {};
        let input = $('.form-control').val();
        let url = `http://api.openweathermap.org/data/2.5/weather?q=${input}&appid=772f2d88cb1fd3a790d48a49eb3d0aed`;
        let response = fetch(url)
        .then(res => res.json())
        .then(data => {
            console.log(data); 
            $('.card-title').html(data.name);
            $('#weather').html(data.weather[0].main);
            $('#temp').html(`${kelvinToCelsius(data.main.temp)} °C`);
            $('.card-img-top').attr('src', `http://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`);})
        .catch(err => console.log(err))
    };
});

    /*$('#search-form').submit(function (e) {
        console.log($('.form-control').val());
        e.preventDefault();
        if ($('.form-control').val()) {
            let input = $('.form-control').val();
            $.ajax({
                url: 'api/hg',
                type: 'POST',
                data: {
                    city: input,
                    csrfmiddlewaretoken: csrf
                },
                success: function (res) {
                    // cities = JSON.parse(res);
                    let template = '';
                    for (let i = 0; i < res['city'].length; i++) {
                        template += `<p>
                        <h4>${res['city'][i]['city']}</h4>
                        <h4>${res['city'][i]['country']}</h4>
                        <h4>${res['city'][i]['wheather']}</h4>`;
                        console.log(res['city'][i]); 
                         
                    } 
                $('#result').html(template); 
                }
            });
        }
    });*/
});
