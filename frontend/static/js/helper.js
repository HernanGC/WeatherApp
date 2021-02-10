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
            class: 'container-fluid'
        },
        children: [{
            type: 'h2',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {},
            children: []
        }, {
            type: 'p',
            attributes: {
                class: ''
            },
            children: []
        }]
    }],
    updateModalChildren() {
        /** Obtengo los elementos children (los de mas abajo) que voy a pintar en el modal */
        let modalChildren = this.children[1].children;
        let elements = ['city', 'weather_main', 'weather_description', 'weather_icon', 'temperature', 'feels_like', 'temp_min', 'temp_max'];
        let count = 0;
        Object.keys(modalChildren).forEach(key => {
            count++;
            modalChildren[key].children = (count < 5) ? [capitalize(weatherObject[elements[key]])] : [`${kelvinToCelsius(weatherObject[elements[key]])} °C`];
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
    return Math.round(Number(temp) - 273.15 * 10 / 10) 
}

const capitalize = function (str) {
    return str[0].toUpperCase() + str.slice(1);
}