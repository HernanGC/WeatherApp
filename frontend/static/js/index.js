$('document').ready(function () {

var csrf = $('input[name=csrfmiddlewaretoken]').val();


const kelvinToCelsius = function (temp) {
    return Math.round(Number(temp) - 273.15 * 10 / 10) 
}


const transientSearch = function () {
    
}

const updateLatestSearch = function (data) {
    fetch('api/get/latestsearch')
    .then(res => res.json())
    .then(data => {
        let resultImg = document.querySelectorAll('.latest-r-img');
        let resultTemp = document.querySelectorAll('.latest-r-temp');
        let resultTitle = document.querySelectorAll('.latest-r-title');
        let resultMain = document.querySelectorAll('.latest-r-main');
        let html = '';
        data.latest_search.forEach((el, index) => {
            let {weather_icon, temperature, city, weather_main} = el;
            resultImg[index].src = `http://openweathermap.org/img/wn/${weather_icon}@2x.png`;
            resultTemp[index].textContent = temperature;
            resultTitle[index].textContent = city;
            resultMain[index].textContent = weather_main;
            html += ``;
            console.log(city);    
        });
    })
    .catch(err => console.log(`An error has ocurred: ${err}`))

}

$('#search-form').submit(function (e) {
    e.preventDefault();
    if ($('.form-control').val()) {
        let input = $('.form-control').val();
        let url = `http://api.openweathermap.org/data/2.5/weather?q=${input}&appid=772f2d88cb1fd3a790d48a49eb3d0aed`;
        fetch(url)
        .then(res => res.json())
        .then(data => {
            // console.log(data); 
            if (data.cod === 200) {
                $('#city').html(data.name);
                $('#weather').html(data.weather[0].main);
                $('#temp').html(`${kelvinToCelsius(data.main.temp)} °C`);
                $('#temp-img').attr('src', `http://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`);
                document.querySelector('.weather-result').classList.remove('hidden');
                $.ajax({
                    url: 'api/add',
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        city: data.name,
                        long: parseInt(data.coord.lon),
                        lat: parseInt(data.coord.lat),
                        weather_main: data.weather[0].main,
                        weather_description: data.weather[0].description,
                        weather_icon: data.weather[0].icon,
                        temperature: parseInt(kelvinToCelsius(data.main.temp)),
                        feels_like: parseInt(data.main.feels_like),
                        temp_min: parseInt(data.main.temp_min),
                        temp_max: parseInt(data.main.temp_max),
                        pressure: parseInt(data.main.pressure),
                        humidity: parseInt(data.main.humidity),
                        visibility: parseInt(data.visibility),
                        wind_speed: parseInt(data.wind.speed),
                        wind_deg: parseInt(data.wind.deg),
                        clouds: parseInt(data.clouds.all),
                    }, success: function (resp) {
                        updateLatestSearch();
                        console.log(resp);
                    }
                });
            } else {
                document.querySelector('.weather-result').classList.remove('hidden');
                $('.card-title').html(data.message);
                $('#weather').html('');
                $('#temp').html('');
                $('.card-img-top').attr('src', '');
            }
        })
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
