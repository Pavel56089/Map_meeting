ymaps.ready(init);
        function init() {
            var map = new ymaps.Map('map', {
            center: [55.75399399999374,37.62209300000001],
            zoom: 10,
            controls: ['geolocationControl', 'zoomControl']
        }),
        firstButton = new ymaps.control.Button({
          data: {
            content:'Добавить себя',
          },
          options: {
            maxWidth: [30, 100, 150],
          }
        });

    map.controls.add(firstButton, {float: 'right'});
        }
