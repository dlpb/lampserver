$( document ).ready(function() {

    var signal = {};
    signal.red = {};
    signal.green = {};

    var status = function(){
        $.ajax({
            url: "/signal",

            success: function( data ) {

                signal.green.state = data.state.green
                signal.red.state = data.state.red

                $( "#red-signal-status span" ).html(data.state.red );
                $( "#green-signal-status span" ).html(data.state.green );

                $("#red-signal-status span").removeClass("off");
                $("#red-signal-status span").removeClass("on");
                $("#red-signal-status span").addClass(data.state.red);

                $("#green-signal-status span").removeClass("off");
                $("#green-signal-status span").removeClass("on");
                $("#green-signal-status span").addClass(data.state.green);
            }
        });

        $.ajax({
            url: "/signal/green",
            success: function( data ) {
                signal.green.lamp = data.state.lamp;
                signal.green.pigear = data.state.pigear;

                $( "#green-lamp-status span" ).html(data.state.lamp );
                $( "#green-pigear-status span" ).html(data.state.pigear );

                $("#green-lamp-status span").removeClass("off");
                $("#green-lamp-status span").removeClass("on");
                $("#green-lamp-status span").addClass(data.state.lamp );

                $("#green-pigear-status span").removeClass("off");
                $("#green-pigear-status span").removeClass("on");
                $("#green-pigear-status span").addClass(data.state.pigear);
            }
        });

        $.ajax({
            url: "/signal/red",
            success: function( data ) {
                signal.red.lamp = data.state.lamp;
                signal.red.pigear = data.state.pigear;

                $( "#red-lamp-status span" ).html(data.state.lamp );
                $( "#red-pigear-status span" ).html(data.state.pigear );

                $("#red-lamp-status span").removeClass("off");
                $("#red-lamp-status span").removeClass("on");
                $("#red-lamp-status span").addClass(data.state.lamp);

                $("#red-pigear-status span").removeClass("off");
                $("#red-pigear-status span").removeClass("on");
                $("#red-pigear-status span").addClass(data.state.pigear);
            }
        });
    };
    status();

    $("#green-signal-button").click(function(event) {
        var toggle = signal.green.state === "on" ? "off" : "on";
        $.post( "/signal/green", {'state':toggle}, function( data ) {
          status();
        });
    });
    $("#green-lamp-button").click(function(event) {
        var toggle = signal.green.lamp === "on" ? "off" : "on";
        $.post( "/signal/green/lamp", {'state':toggle}, function( data ) {
          status();
        });
    });
    $("#green-pigear-button").click(function(event) {
        var toggle = signal.green.pigear === "on" ? "off" : "on";
        $.post( "/signal/green/pigear", {'state':toggle}, function( data ) {
          status();
        });
    });
    $("#red-signal-button").click(function(event) {
        var toggle = signal.red.state === "on" ? "off" : "on";
        $.post( "/signal/red", {'state':toggle}, function( data ) {
          status();
        });
    });
    $("#red-lamp-button").click(function(event) {
        var toggle = signal.red.lamp === "on" ? "off" : "on";
        $.post( "/signal/red/lamp", {'state':toggle}, function( data ) {
          status();
        });
    });
    $("#red-pigear-button").click(function(event) {
        var toggle = signal.red.pigear === "on" ? "off" : "on";
        $.post( "/signal/red/pigear", {'state':toggle}, function( data ) {
          status();
        });
    });
});