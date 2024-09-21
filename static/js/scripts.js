/*!
* Start Bootstrap - Creative v7.0.7 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
});
function filterCars(status) {
    if (status === 'available') {
      document.getElementById('filter-title').innerText = 'Available Cars';
      $(".available-car").show();
      $(".in-use-car").hide();
      $(".out-of-order-car").hide();
      $(".show-status").hide();
    } else if (status === 'in-use') {
      document.getElementById('filter-title').innerText = 'In-Use Cars';
      $(".available-car").hide();
      $(".in-use-car").show();
      $(".out-of-order-car").hide();
      $(".show-status").hide();
    } else if (status === 'out-of-order') {
      document.getElementById('filter-title').innerText = 'Out of Order Cars';
      $(".available-car").hide();
      $(".in-use-car").hide();
      $(".out-of-order-car").show();
      $(".show-status").hide();
    } else {
      document.getElementById('filter-title').innerText = 'All Cars';
      $(".available-car").show();
      $(".in-use-car").show();
      $(".out-of-order-car").show();
      $(".show-status").show();
    }
  };
function editCar() {
    var inUseNow = document.getElementById('status').value;
    console.log(inUseNow);
    if ( inUseNow === 'in-use') {
        $('#edit-in-use').show();
        $('#edit-in-use2').show();
        document.getElementById('return-date').required = true;
        document.getElementById('return-time').required = true;
        document.getElementById('pickup-date').required = true;
        document.getElementById('pickup-time').required = true;

        const rd_attr = document.createAttribute("name");
        rd_attr.value = "return_date";
        const rd_element = document.getElementById("return-date");
        rd_element.setAttributeNode(rd_attr);

        const rt_attr = document.createAttribute("name");
        rt_attr.value = "return_time";
        const rt_element = document.getElementById("return-time");
        rt_element.setAttributeNode(rt_attr);

        const pd_attr = document.createAttribute("name");
        pd_attr.value = "pickup_date";
        const pd_element = document.getElementById("pickup-date");
        pd_element.setAttributeNode(pd_attr);

        const pt_attr = document.createAttribute("name");
        pt_attr.value = "pickup_time";
        const pt_element = document.getElementById("pickup-time");
        pt_element.setAttributeNode(pt_attr);
    } else {
        $('#edit-in-use').hide();
        $('#edit-in-use2').hide();
        document.getElementById('return-date').required = false;
        document.getElementById('return-time').required = false;
        document.getElementById('pickup-date').required = false;
        document.getElementById('pickup-time').required = false;

        const rd_element = document.getElementById("return-date");
        const rd_attr = rd_element.getAttributeNode("name");
        rd_element.removeAttributeNode(rd_attr);

        const rt_element = document.getElementById("return-time");
        const rt_attr = rt_element.getAttributeNode("name");
        rt_element.removeAttributeNode(rt_attr);

        const pd_element = document.getElementById("pickup-date");
        const pd_attr = pd_element.getAttributeNode("name");
        pd_element.removeAttributeNode(pd_attr);

        const pt_element = document.getElementById("pickup-time");
        const pt_attr = pt_element.getAttributeNode("name");
        pt_element.removeAttributeNode(pt_attr);
    }
};
