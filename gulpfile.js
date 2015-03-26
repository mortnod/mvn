"use strict";

var gulp = require("gulp");

// Loads the plugins without having to list all of them, but you need
// to call them as $.pluginname
var $ = require("gulp-load-plugins")();

// "del" is used to clean out directories and such
var del = require("del");

// BrowserSync isn't a gulp package, and needs to be loaded manually
var browserSync = require("browser-sync");

// merge is used to merge the output from two different streams into the same stream
var merge = require("merge-stream");

// Need a command for reloading webpages using BrowserSync
var reload = browserSync.reload;

// And define a variable that BrowserSync uses in its function
var bs;


//--------------------------------------------------
// GULP HELPER TASKS (Don't run these manually)
//--------------------------------------------------

// Deletes the output directories (dev -> _site, prod -> _production)
gulp.task("clean:dev", del.bind(null, ["_site"]));
gulp.task("clean:prod", del.bind(null, ["_production"]));

// Runs the build command for Jekyll to compile the site locally
gulp.task("jekyll", $.shell.task("jekyll build"));
gulp.task("jekyll-rebuild", ["jekyll"], function () {
  reload;
});

// Compiles the SASS files and moves them into the "assets/stylesheets" directory
gulp.task("styles", function () {
  // Looks at the main.scss file for what to include and creates a main.css file
  return gulp.src("src/assets/scss/main.scss")
    .pipe($.sass({
      errLogToConsole: true
    }))
    // AutoPrefix your CSS so it works between browsers
    .pipe($.autoprefixer("last 1 version", { cascade: true }))
    // Directory your CSS file goes to
    .pipe(gulp.dest("src/assets/css/"))
    .pipe(gulp.dest("_site/assets/css/"))
    // Outputs the size of the CSS file
    .pipe($.size({title: "styles"}))
    // Injects the CSS changes to your browser since Jekyll doesn't rebuild the CSS
    .pipe(reload({stream: true}));
});

// Optimizes the images and copy them to '_production'
gulp.task("images", function () {
  return gulp.src("src/assets/img/**")
    .pipe($.changed("_production/assets/img"))
    .pipe($.imagemin({
      // Lossless conversion to progressive JPGs
      progressive: true,
      // Interlace GIFs for progressive rendering
      interlaced: true
    }))
    .pipe(gulp.dest("_production/assets/img"))
    .pipe($.size({title: "img"}));
});

// Copy fonts from '_site' to '_production'
gulp.task("copy:fonts", function () {
  return gulp.src("src/assets/fonts/**")
    .pipe(gulp.dest("_production/assets/fonts"))
    .pipe($.size({ title: "fonts" }));
});

// Copy xml and txt files from '_site' to '_production'
gulp.task("copy:txt", function () {
  return gulp.src(["_site/*.txt", "_site/*.xml"])
    .pipe(gulp.dest("_production"))
    .pipe($.size({ title: "xml & txt" }))
});

// Optimizes all the CSS, HTML and concats the JS etc
gulp.task("html", ["styles"], function () {
  var assets = $.useref.assets({searchPath: "_site"});

  return gulp.src("_site/**/*.html")
    .pipe(assets)
    // Concatenate .js files and preserve important comments
    .pipe($.if("*.js", $.uglify({preserveComments: "some"})))
    // Minify CSS
    .pipe($.if("*.css", $.minifyCss()))
    // Start cache busting the files
    .pipe($.revAll({ ignore: [".eot", ".svg", ".ttf", ".woff"] }))
    .pipe(assets.restore())
    // Concatenate your files based on what you specified in _layout/header.html
    .pipe($.useref())
    // Replace the asset names with their cache busted names
    .pipe($.revReplace())
    // Minify HTML
    .pipe($.if("*.html", $.htmlmin({
      removeComments: true,
      removeCommentsFromCDATA: true,
      removeCDATASectionsFromCDATA: true,
      collapseWhitespace: true,
      collapseBooleanAttributes: true,
      removeAttributeQuotes: true,
      removeRedundantAttributes: true
    })))
    // Send the output to the correct folder
    .pipe(gulp.dest("_production"))
    .pipe($.size({title: "optimizations"}));
});


// Run JS Hint against your JS
gulp.task("jslint", function () {
  gulp.src("./_site/assets/js/*.js")
    // Checks your JS code quality against your .jshintrc file
    .pipe($.jshint(".jshintrc"))
    .pipe($.jshint.reporter());
});

// Runs "jekyll doctor" on your site to check for errors with your configuration
// and will check for URL errors a well
gulp.task("doctor", $.shell.task("jekyll doctor"));

// Builds the site but doesn"t serve it to you
gulp.task("build", ["jekyll", "styles"], function () {});

// BrowserSync will serve our site on a local server for us and other devices to use
// It will also autoreload across all devices as well as keep the viewport synchronized
// between them.
gulp.task("serve:dev", ["build"], function () {
  bs = browserSync({
    notify: true,
    // tunnel: "",
    server: {
      baseDir: "_site"
    }
  });
});

// These tasks will look for files that change while serving and will auto-regenerate or
// reload the website accordingly. Update or add other files you need to be watched.
gulp.task("watch", function () {
  gulp.watch(["src/**/*.md", "src/**/*.html", "src/**/*.xml", "src/**/*.txt", "src/**/*.js"], ["jekyll-rebuild"]);
  gulp.watch(["_site/assets/css/*.css"], reload);
  gulp.watch(["src/assets/scss/**/*.scss"], ["styles"]);
});




//--------------------------------------------------
// GULP TASKS (The ones you should actually use)
//--------------------------------------------------

// GULP: Compiles files, starts server and watch for changes. Use for development.
gulp.task("default", ["serve:dev", "watch"]);


// GULP CHECK: Checks your CSS, JS and Jekyll for errors
gulp.task("check", ["jslint", "doctor"], function () {
  // Better hope nothing is wrong.
});

// GULP PUBLISH: Builds your site with "build" (same as 'gulp') and then
// runs optimizations such as minification, imagemin and cache busting.
// Outputs to "./_production"
gulp.task("publish", function () {
  gulp.start("build", "html", "copy:txt", "images", "copy:fonts");
});

// GULP SERVE:PROD: Serve the site after optimizations to see that everything looks fine
gulp.task("serve:prod", function () {
  bs = browserSync({
    notify: false,
    // tunnel: true,
    server: {
      baseDir: "_production"
    }
  });
});

// GULP DEPLOY: Task to upload your site via Rsync to your server
gulp.task("deploy", function () {
  // Load in the variables needed for our Rsync synchronization
  var secret = require("./rsync-credentials.json");

  return gulp.src("_production/**")
    .pipe($.rsync({
      // This uploads the contents of "root", instead of the folder
      root: "_production",
      // Find your username, hostname and destination from your rsync-credentials.json
      hostname: secret.hostname,
      username: secret.username,
      destination: secret.destination,
      // Incremental uploading, adds a small delay but minimizes the amount of files transferred
      incremental: true,
      // Shows the progress on your files while uploading
      progress: true
  }));
});