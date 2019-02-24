ymaps.ready(init);
        function init() {
            var map = new ymaps.Map('map', {
            center: [59.93772, 30.313622],
            zoom: 10,
            controls: ['geolocationControl', 'zoomControl']
        }),
        firstButton = new ymaps.control.Button("Добавить себя на карту");

    map.controls.add(firstButton, {float: 'right'});
        }
