export let weatherObject = {
    'id':                  '',
    'city':                '',
    'long':                '',
    'lat':                 '',
    'weather_main':        '',
    'weather_description': '',
    'weather_icon':        '',
    'temperature':         '',
    'feels_like':          '',
    'temp_min':            '',
    'temp_max':            '',
    'pressure':            '',
    'humidity':            '',
    'visibility':          '',
    'wind_speed':          '',
    'wind_deg':            '',
    'clouds':              '',
    setObjectState(data) {
        Object.keys(data).forEach(key => {
            this[key] = data[key];
        });
        return this;
    }
};
export let modal = {
    type: 'div',
    parent: document.body,
    attributes: {
        class: 'weather-modal'
    },
    children: [{
        type: 'button',
        attributes: {
            class: 'close-modal',
        },
        children: ['x']
    }, {
        type: 'div',
        attributes: {
            class: 'modal-content-h'
        },
        children: [{
            type: 'h4',
            attributes: {
                class: 'modal-r-weather'
            },
            children: []
        }, {
            type: 'h1',
            attributes: {
                class: 'modal-r-main'
            },
            children: []
        }, {
            type: 'h3',
            attributes: {
                class: 'modal-r-descr'
            },
            children: []
        }, {
            type: 'img',
            attributes: {
                class: 'modal-r-img',
                src: ''
            },
            children: []
        }, {
            type: 'h5',
            attributes: {
                class: 'modal-r-curr'
            },
            children: []
        }, {
            type: 'h5',
            attributes: {
                class: 'modal-r-feel'
            },
            children: []
        }, {
            type: 'h5',
            attributes: {
                class: 'modal-r-max'
            },
            children: []
        }, {
            type: 'h5',
            attributes: {
                class: 'modal-r-min'
            },
            children: []
        }]
    }],
    updateModalChildren() {
        /** Obtengo los elementos children (los de mas abajo) que voy a pintar en el modal */
        let modalChildren = this.children[1].children;
        let elements = ['weather_main', 'city', 'weather_description', 'weather_icon', 'temperature', 'feels_like', 'temp_min', 'temp_max'];
        Object.keys(modalChildren).forEach(key => {
            if (elements[key] == 'weather_icon') {
                modalChildren[key].attributes.src = `http://openweathermap.org/img/wn/${weatherObject[elements[key]]}@2x.png`
            }
            modalChildren[key].children = (elements[key] == 'weather_icon') ? [] : [weatherObject[elements[key]]];
        });
        return this;
    }
};
export const overlay = {
    type: 'div',
    parent: document.body,
    attributes: {
        class: 'overlay'
    },
    children: []
};
export const loader = {
    type: 'div',
    parent: document.getElementById('result-container'),
    attributes: {
        id: 'loading'
    },
    children: []
};

export const kelvinToCelsius = function (temp) {
    // return Math.round(Number(temp) - 273.15 * 10 / 10) 
    return temp;
}

const capitalize = function (str) {
    return str[0].toUpperCase() + str.slice(1);
}