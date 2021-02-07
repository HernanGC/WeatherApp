document.addEventListener('DOMContentLoaded', function () {

var csrf = $('input[name=csrfmiddlewaretoken]').val();

const searchForm  = document.getElementById('search-form');
const searchInput = document.querySelector('.form-control');

const loader = document.getElementById('loading');
const weatherResult = document.getElementById('weather-result');

const searchResult = {
    city:    document.getElementById('city'),
    weather: document.getElementById('weather'),
    temp:    document.getElementById('temp'),
    icon:    document.getElementById('temp-img')
};


/** MAIN FUNCTIONS */

searchForm.addEventListener('submit', function (e) {
    e.preventDefault();
    if (isSearchRepeated()) {
        hideElement(weatherResult);
        showElement(loader);
        clearInput();
        return;
    }
    hideElement(weatherResult);
    showElement(loader);
    let bodyResponse = '';
    
    let searchInputValue = {
        search: searchInput.value,
    };
    if (searchInputValue) {
        fetch('api/searchrequest', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf
            },
            body: JSON.stringify(searchInputValue)
        })
        .then(res => res.json())
        .then(data => {
            bodyResponse = data.body;
            hideElement(loader);
            showElement(weatherResult);
            clearInput();
            if (bodyResponse && data.msg == 'success') {
                updateResult(bodyResponse);
                updateLatestSearch();
                console.log(typeof data.body);
            } else {
                console.log(typeof data.body);
                updateResult(bodyResponse);
            }
        })
        .catch(err => console.log(`ERRRRRRR ${err}`))
    }
});

const updateLatestSearch = function () {
    fetch('api/get/latestsearch')
    .then(res => res.json())
    .then(data => {
        let resultImg   = document.querySelectorAll('.latest-r-img');
        let resultTemp  = document.querySelectorAll('.latest-r-temp');
        let resultTitle = document.querySelectorAll('.latest-r-title');
        let resultMain  = document.querySelectorAll('.latest-r-main');
        data.latest_search.forEach((el, index) => {
            let {weather_icon, temperature, city, weather_main} = el;
            resultImg[index].src = `http://openweathermap.org/img/wn/${weather_icon}@2x.png`;
            resultTemp[index].textContent = `${kelvinToCelsius(temperature)} °C`;
            resultTitle[index].textContent = city;
            resultMain[index].textContent = weather_main;
        });
    })
    .catch(err => console.log(`An error has ocurred: ${err}`))

}

const updateResult = function (bodyResponse) {
    
    if (typeof bodyResponse === 'object') {
        searchResult.city.textContent = bodyResponse.city;
        searchResult.weather.textContent = bodyResponse.weather;
        searchResult.temp.textContent = `${kelvinToCelsius(bodyResponse.temperature)} °C`;
        searchResult.icon.src = `http://openweathermap.org/img/wn/${bodyResponse.icon}@2x.png`;
    } else {
        resetSearchResult();
        searchResult.city.textContent = bodyResponse;
    }
    
    
}


/** HELPERS */


const isSearchRepeated = function () {
    console.log(searchInput.value);
    console.log(searchResult.city);
    return searchInput.value.toLowerCase() == searchResult.city.textContent.toLowerCase();
}


const kelvinToCelsius = function (temp) {
    return Math.round(Number(temp) - 273.15 * 10 / 10) 
}

const clearInput = function () {
    document.querySelector('.form-control').value = '';
}

const hideElement = function (element) {
    element.classList.add('hidden');
}

const showElement = function (element) {
    element.classList.remove('hidden');
}

const resetSearchResult = function () {
    searchResult.city.textContent = '';
    searchResult.weather.textContent = '';
    searchResult.temp.textContent = '';
    searchResult.icon.src = '';
}

const sleeping = async function (ms) {
    return await sleep(ms);
}


async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

const isLoading = function () {

}

});