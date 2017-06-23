
riot.tag2('test', '<div class="col s12 m6"> <div class="row"> <div class="col s4 center" each="{num in data}"><span>{num}</span></div> </div> </div>', '', '', function(opts) {
var self;

self = this;

this.on('mount', function() {
  self.data = ['1', '2', '3'];
  return self.update({
    data: self.data
  });
});
});

riot.tag2('top-menu-tag', '<nav class="z-depth-0"> <div class="nav-wrapper container"><a class="brand-logo" href="#">Logo</a> <ul class="right hide-on-med-and-down" id="nav-mobile"> <li><a href="#">Link 1</a></li> <li><a href="#">Link 2</a></li> <li><a href="#">Link 3</a></li> </ul> </div> </nav>', '', '', function(opts) {
});