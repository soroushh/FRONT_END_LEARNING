const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Hello, Vue!'
    }
});

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Hello Vue.'
    }
});
