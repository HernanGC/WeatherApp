import { modal, overlay, loader, weatherObject, kelvinToCelsius} from '../js/helper.js';


document.addEventListener('DOMContentLoaded', function () {

var csrf = $('input[name=csrfmiddlewaretoken]').val();

const searchForm  = document.getElementById('search-form');
const searchInput = document.querySelector('.form-control');

const weatherResultAll = document.querySelectorAll('.card-weather');

// const loader = document.getElementById('loading');
const weatherResult = document.getElementById('weather-result');
const searchCityResult = document.getElementById('search-result');


const searchResult = {
    id:      document.getElementById('weather-id'),
    city:    document.getElementById('city'),
    weather: document.getElementById('weather'),
    temp:    document.getElementById('temp'),
    icon:    document.getElementById('temp-img')
};


/** MAIN FUNCTIONS */



searchForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const loaderElement = createElement(loader);
    hideElement(weatherResult);
    let bodyResponse = '';
    
    let searchInputValue = searchInput.value;
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
            weatherObject.setObjectState(bodyResponse);
            loaderElement.remove();
            showElement(weatherResult);
            clearInput();
            updateResult(bodyResponse);
            updateLatestSearch(data.msg);
        })
        .catch(err => console.log(`ERRRRRRR ${err}`))
    }
});


for (let weatherRes of weatherResultAll) {
    weatherRes.addEventListener('click', function () {
        const weatherModalExists = document.querySelector('.weather-modal') ?? false;
        // TODO: Mejorar esta forma de obtener el id en el dom
        let objectId = weatherRes.children[1].children[0].textContent;
        console.log(objectId);
        if (objectId) {
            fetch('api/searchbyid', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrf
                },
                body: JSON.stringify(objectId)
            })
            .then(res => res.json())
            .then(data => {
                weatherObject.setObjectState(data.body);
                modal.updateModalChildren();
                if (!document.querySelector('.weather-modal')) {
                    let weatherModal = createElement(modal);
                    let overlayEffect = createElement(overlay);
                    weatherModal.children[0].addEventListener('click', function () {
                        weatherModal.remove();
                        overlayEffect.remove();
                    });  
                    document.addEventListener('keydown', function (e) {
                        if (e.key === 'Escape') {
                            weatherModal.remove();
                            overlayEffect.remove();
                        }
                    });
                    overlayEffect.addEventListener('click', function () {
                        weatherModal.remove();
                        overlayEffect.remove();
                    });
                }
            })
            .catch(err => console.log(`Error: ${err}`))    
        }
    });
}


const updateLatestSearch = function (msg) {
    let dataToSend =  msg;
    fetch('api/get/latestsearch', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        body: JSON.stringify(dataToSend)
    })
    .then(res => res.json())
    .then(data => {
        let resultId    = document.querySelectorAll('.latest-r-id'); 
        let resultImg   = document.querySelectorAll('.latest-r-img');
        let resultTemp  = document.querySelectorAll('.latest-r-temp');
        let resultTitle = document.querySelectorAll('.latest-r-title');
        let resultMain  = document.querySelectorAll('.latest-r-main');
        data.latest_search.forEach((el, index) => {
            let {id, weather_icon, temperature, city, weather_main} = el;
            resultId[index].textContent = id;
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
        searchResult.id.textContent = bodyResponse.id;
        searchResult.city.textContent = bodyResponse.city;
        searchResult.weather.textContent = bodyResponse.weather_main;
        searchResult.temp.textContent = `${kelvinToCelsius(bodyResponse.temperature)} °C`;
        searchResult.icon.src = `http://openweathermap.org/img/wn/${bodyResponse.weather_icon}@2x.png`;
    } else {
        resetSearchResult();
        searchResult.city.textContent = bodyResponse;
    }
}


/** HELPERS */


const createElement = function ({
    type,
    parent,
    attributes = {},
    children = []
}) {
   const element = document.createElement(type);

   Object.keys(attributes).forEach((key) => {
        element.setAttribute(key, attributes[key]);
   });

   children.forEach(child => {
       if (typeof child == 'object') {
           return createElement({...child, parent: element })
       }
       const textNode = document.createTextNode(child);
       element.appendChild(textNode);
   });

   parent.appendChild(element);
   return element;
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
});