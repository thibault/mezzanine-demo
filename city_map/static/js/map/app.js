var App = {
    Models: {},
    Collections: {},
    Views: {},
    Routers: {},
    Config: {}
};

App.Routers.MapRouter = Backbone.Router.extend({
    initialize: function(options) {
        this.route('', 'map');
        this.route(':slug/', 'pointOfInterest');
    },
    map: function() {
        console.log('map');
    },
    pointOfInterest: function(slug) {
        console.log('point !');
    }
});

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
});

//MarkerView has no element
App.Views.MarkerView = Backbone.View.extend({

    initialize: function(options) {
        this.map = options.map,
        this.marker = L.marker([this.model.get('lat'), this.model.get('lng')]);

        // Create the marker popup
        var popup = document.createElement('a');
        popup.href = App.Config.mapUrl + this.model.get('slug') + '/';
        popup.innerHTML = this.model.get('name');

        // We have to bind the event here, because leaflets prevents
        // the click event to buble outside the map element
        var slug = this.model.get('slug');
        popup.onclick = function(event) {
            event.preventDefault();
            Backbone.history.navigate(slug);
        };
        this.marker.bindPopup(popup);
    },

    render: function() {    
        // All we have to do is add the marker to the map
        // (Leaflet API)
        this.marker.addTo(this.map);
        return this;
    }
});

//MapView renders a map to the #map element
App.Views.MapView = Backbone.View.extend({
    initialize: function(options) {
        this.map = options.map;
        this.markers = new App.Collections.MarkerCollection();
        this.listenTo(this.markers, "reset", this.render);
        this.markers.fetch({ reset: true });
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
        view.render();
    }
});

$(function() {
    var mapRouter = new App.Routers.MapRouter();
    Backbone.history.start({
        pushState: true,
        root: App.Config.mapUrl,
    });
});
