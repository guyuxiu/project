#!/usr/bin/python3
# -*- coding: UTF-8 -*-
all = "adsfad"
html_content = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Layouts &raquo; Split-Centered</title>
  <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no' />
  <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
  <script type="text/javascript" src="https://assets.pyecharts.org/assets/themes/chalk.js"></script>
  <!-- Demo Dependencies -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.6/holder.js" type="text/javascript"></script>
  <script>
    Holder.addTheme("white", {
      bg: "#fff",
      fg: "#a7a7a7",
      size: 10
    });
  </script>

  <!-- Dashboard -->
  <link rel="stylesheet" type="text/css"
    href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css" />
  <link rel="stylesheet" type="text/css" href="keen-dashboards.css" />
</head>

<body class="keen-dashboard">

  <div class="container">
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="../">
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="76.39 132.243 15.35 22" width="20" height="20" fill="#777">
            <defs>
              <path id="a"
                d="M88.31 136.63c.29-.28.43-.63.43-1.05 0-.41-.14-.76-.43-1.04-.08-.09-.78-.78-.86-.87-.29-.28-.64-.43-1.05-.43-.41 0-.76.15-1.05.43-.75.75-6.78 6.77-7.53 7.53-.29.28-.43.63-.43 1.04 0 .42.14.76.43 1.05.75.75 6.78 6.77 7.53 7.53.29.28.64.42 1.05.42.41 0 .76-.14 1.05-.42.08-.09.78-.78.86-.87.29-.29.43-.63.43-1.04 0-.41-.14-.76-.43-1.05-.37-.38-2.24-2.25-5.61-5.61 3.37-3.37 5.24-5.24 5.61-5.62z" />
            </defs>
            <use xlink:href="#a" />
            <use xlink:href="#a" />
          </svg>
        </a>
        <a class="navbar-brand" href="./">Layouts &raquo; Split Centered</a>
      </div>
      <div class="navbar-collapse">
        <ul class="navbar-nav nav main-nav">
          <li><a href="https://keen.io">Home</a></li>
          <li><a href="https://keen.io/team">Team</a></li>
          <li><a href="https://github.com/keenlabs/dashboards/tree/gh-pages/layouts/hero-sidebar">Source</a>
          </li>
          <li><a href="https://groups.google.com/forum/#!forum/keen-io-devs">Community</a></li>
          <li><a href="http://stackoverflow.com/questions/tagged/keen-io?sort=newest&pageSize=15">Technical
              Support</a></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="container grid grid-split-centered">
    <div class="grid-split">
      <div class="grid-split-column">
        <div class="chart-wrapper">
          <div class="chart-title">
            Cell Title
          </div>
          <div class="chart-stage">
            <img data-src="holder.js/100px120?theme=white">
          </div>
          <div class="chart-notes">
            Notes about this chart
          </div>
        </div>
        <div class="chart-wrapper">
          <div class="chart-title">
            Cell Title
          </div>
          <div class="chart-stage">
            <img data-src="holder.js/100px120?theme=white">
          </div>
          <div class="chart-notes">
            Notes about this chart
          </div>
        </div>
      </div>
      <div class="grid-split-column grid-split-column--centered">
        <div class="chart-wrapper">
          <div class="chart-title">
            总播放量
          </div>
          <div class="chart-stage">
            {all}
          </div>
          <div class="chart-notes">
            Notes about this chart
          </div>
        </div>
      </div>
      <div class="grid-split-column">
        <div class="chart-wrapper">
          <div class="chart-title">
            Cell Title
          </div>
          <div class="chart-stage">
            <img data-src="holder.js/100px120?theme=white">
          </div>
          <div class="chart-notes">
            Notes about this chart
          </div>
        </div>
        <div class="chart-wrapper">
          <div class="chart-title">
            Cell Title
          </div>
          <div class="chart-stage">
            <img data-src="holder.js/100px120?theme=white">
          </div>
          <div class="chart-notes">
            Notes about this chart
          </div>
        </div>
      </div>
    </div>

    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
    <div class="chart-wrapper">
      <div class="chart-title">
        Cell Title
      </div>
      <div class="chart-stage">
        <img data-src="holder.js/100px120?theme=white">
      </div>
      <div class="chart-notes">
        Notes about this chart
      </div>
    </div>
  </div>

  <div class="container">
    <p class="small text-muted">Built with &#9829; by <a href="https://keen.io">Keen IO</a></p>
  </div>

  <!-- Project Analytics -->  <script>
    function toggleMenu() {
      const toggleBtn = document.querySelector('.navbar-toggle');

      toggleBtn.addEventListener('click', (e) => {
        let menu;
        if (e.currentTarget.dataset.target) {
          menu = document.querySelector(e.currentTarget.dataset.target);
        }
        if (menu) menu.classList.toggle('collapsed');
      });
    }

    window.addEventListener('DOMContentLoaded', toggleMenu);
  </script>
</body>

</html>
"""

