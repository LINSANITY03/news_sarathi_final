function switchChannel(el) {
  // find all the elements in your channel list and loop over them
  Array.prototype.slice.call(document.querySelectorAll('ul[data-tag="channelList"] li')).forEach(function (element) {
    // remove the selected class
    element.classList.remove('selected');
  });
  // add the selected class to the element that was clicked
  el.classList.add('selected');
}


function callMe(el) {
  if (el == 'UL_1') {
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
      if (this.readyState !== 4) return;
      if (this.status !== 200) return; // or whatever error handling you want
      document.getElementById("ns_setting_section").innerHTML = this.responseText;
    };
    xhr.open("GET", '/ns_setting_1', true);
    xhr.send();
  }

  else if (el == 'UL_2') {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {

      if (this.readyState !== 4) return;
      if (this.status !== 200) return; // or whatever error handling you want
      document.getElementById("ns_setting_section").innerHTML = this.responseText;
    };
    xhr.open("GET", '/ns_setting_2', true);
    xhr.send();
  }

  else if (el == 'UL_3') {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (this.readyState !== 4) return;
      if (this.status !== 200) return; // or whatever error handling you want
      document.getElementById("ns_setting_section").innerHTML = this.responseText;
    };
    xhr.open("GET", '/ns_setting_3', true);
    xhr.send();
  }

  else if (el == 'UL_4') {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (this.readyState !== 4) return;
      if (this.status !== 200) return; // or whatever error handling you want
      document.getElementById("ns_setting_section").innerHTML = this.responseText;
    };
    xhr.open("GET", '/ns_setting_4', true);
    xhr.send();
  }

}