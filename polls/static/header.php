<!DOCTYPE html>
 <html lang="en">
 <head>
 <title>index html</title>
 <meta http-equiv="content-type" content="text/html; charset=utf-8" />
<!-- Material Design Stylesheet--> 

<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.lime-orange.min.css">
<!-- define colors https://getmdl.io/customize/index.html -->
<script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>

 <!--<link rel="stylesheet" href="style.css" type="text/css" />
 <link rel="stylesheet" href="w3.css"> -->

 </head>
 
 <body>

<!-- Uses a transparent header that draws on top of the layout's background -->
<style>
.demo-layout-transparent {
  background: url(flat.jpg) center / cover;
}
.demo-layout-transparent .mdl-layout__header,
.demo-layout-transparent .mdl-layout__drawer-button {
  /* This background is dark, so we set text to white. Use 87% black instead if
     your background is light. */
  color: white;
}
</style>

<div class="demo-layout-transparent mdl-layout mdl-js-layout">
  <header class="mdl-layout__header mdl-layout__header--transparent">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">in aeternum</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class="mdl-layout-spacer"></div>
      <!-- Navigation -->
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="index.html">Home</a>
        <a class="mdl-navigation__link" href="information.html">Information</a>
        <a class="mdl-navigation__link" href="https://inaeternumblog.wordpress.com">Projektblog</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">in aeternum</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="index.html">Home</a>
      <a class="mdl-navigation__link" href="information.html">Information</a>
      <a class="mdl-navigation__link" href="https://inaeternumblog.wordpress.com">Projektblog</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
  </main>
</div>