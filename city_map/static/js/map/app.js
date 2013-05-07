var App = {
    Models: {},
    Collections: {},
    Views: {},
    Routers: {},
    Config: {},
    start: function(map) {
        var mapRouter = new App.Routers.MapRouter({ map: map });
        Backbone.history.start({
            pushState: true,
            root: App.Config.mapUrl,
            silent: true,
        });
    }
};

App.Models.Marker = Backbone.Model.extend({
    // name
    // description
    // lat, lng
    // url
});

App.Collections.MarkerCollection = Backbone.Collection.extend({
    model: App.Models.Marker,
    initialize: function() {
        this.url = App.Config.markerCollectionUrl;
    },
    getBySlug: function(slug) {
        return this.findWhere({ slug: slug });
    }
});

//MarkerView has no element
App.Views.MarkerView = Backbone.View.extend({

    id: "map-data",
    initialize: function(options) {
        this.map = options.map,

        // Create the marker using leaflet api
        this.marker = L.marker([this.model.get('lat'), this.model.get('lng')]);

        // Create the marker popup
        var popup = document.createElement('a');
        popup.href = App.Config.mapUrl + this.model.get('slug') + '/';
        popup.innerHTML = this.model.get('name');

        // We have to bind the event here, because leaflets prevents
        // the click event to bubble outside the map element
        var slug = this.model.get('slug');
        popup.onclick = function(event) {
            event.preventDefault();
            Backbone.history.navigate(slug + '/', true);
        };
        this.marker.bindPopup(popup);

        // Render the marker to the map
        // (Leaflet API)
        this.marker.addTo(this.map);
    }
});

//MapView renders a map to the #map element
App.Views.MapView = Backbone.View.extend({
    initialize: function(options) {
        this.map = options.map;
        this.markers = new App.Collections.MarkerCollection();
        this.listenTo(this.markers, "reset", this.render);
        this.markers.fetch({ reset: true });
        this.markerViews = [];
    },
    render: function() {
        this.markers.each(this.addOne, this);
        return this;
    },
    addOne: function(marker) {
        var view = new App.Views.MarkerView({
            model: marker,
            map: this.map
        });
        this.markerViews.push(view);
    }
});

App.Views.TitleView = Backbone.View.extend({
    render: function() {
        this.$el.html(this.model.get('name'));
    }
});

App.Routers.MapRouter = Backbone.Router.extend({
    initialize: function(options) {
        this.route('', 'map');
        this.route(':slug/', 'pointOfInterest');
        this.mapView = new App.Views.MapView({ map: options.map });
        this.titleView = new App.Views.TitleView({ el: $('h1') });
    },
    map: function() {
        // Display the basic map information
        console.log('Router: map');
    },
    pointOfInterest: function(slug) {
        // Display a single point of interest
        console.log('Router: poi ' + slug);

        var marker = this.mapView.markers.getBySlug(slug);

        // Render the title
        this.titleView.model = marker;
        this.titleView.render();
    }
});
