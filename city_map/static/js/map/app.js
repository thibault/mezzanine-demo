var App = {
    Models: {},
    Collections: {},
    Views: {}
};

App.Models.Marker = Backbone.Model.extend({
    // name
    // description
    // lat, lng
    // url
});

App.Collections.MarkerCollection = Backbone.Collection.extend({
    model: App.Models.Marker,
    url: markerCollectionUrl
});

//MarkerView has no element
App.Views.MarkerView = Backbone.View.extend({

    initialize: function(options) {
        this.map = options.map,
        this.marker = L.marker([this.model.get('lat'), this.model.get('lng')]);
    },

    render: function() {    
        //append marker to the map
        this.marker.addTo(this.map);
        this.marker.bindPopup(this.model.get('name'));

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
});
