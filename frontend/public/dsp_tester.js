function rand() {
    return Math.round(Math.random() * 100);
  }
  
  function canvasIsSupported() {
    return !!window.document.createElement("canvas").getContext;
  }
  
  function safeParse(potentialJSON) {
    let json = null;
    try {
      json = JSON.parse(potentialJSON);
    } catch (e) {
      console.error(
        "JSON in tag seems not to be valid, maybe head over to https://jsonlint.com"
      );
    }
    return json;
  }
  
  function makeEl(tag, attrs) {
    let i, el;
  
    el = document.createElement(tag);
    if (attrs && attrs.length > 0 && attrs.length % 2 == 0) {
      for (i = 0; i < attrs.length; i = i + 2) {
        el.setAttribute(attrs[i], attrs[i + 1]);
      }
    }
    return el;
  }
  
  var gameContainerID;
  
  // Function for formatting timestamp
  function formatDate(timestamp) {
    const date = new Date(timestamp);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
  
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  }
  
  // Function for Checking Impression and Viewed Events
  function checkImpressionAndView(sendEvent, game_container, properties) {
    // Record Impression (Check if Game Container is Loaded on Document with the creative)
    sendEvent("impression");
  
    // Record Creative Viewed
    let visibilityTimer;
  
    // Create an Intersection Observer
    let observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            // Element is visible, start the timer with event function
            visibilityTimer = setTimeout(function () {
              sendEvent("viewed");
            }, properties.allotedTime);
          } else {
            // Element is not visible, clear the timer
            clearTimeout(visibilityTimer);
          }
        });
      },
      {
        threshold: properties.percentage, // % of the element must be visible
      }
    );
  
    // Observe the target element
    observer.observe(game_container);
  }
  
  function waitForCanvasAndCheck() {
    const observer = new MutationObserver((mutations, obs) => {
      const game_container = document.getElementById(gameContainerID);
      if (game_container) {
        checkImpressionAndView(sendEvent, game_container, {
          percentage: 0.5,
          allotedTime: 1000,
        });
        obs.disconnect(); // Stop observing once the game_container is found
      }
    });
  
    observer.observe(document.body, {
      childList: true, // Observe direct children
      subtree: true, // Observe all descendants
      attributes: false,
      characterData: false,
    });
  }
  
  function sendEvent(eventType, dsp_data = params, detailData = {}) {
    let timestamp = formatDate(new Date().getTime());
  
    let eventData = {
      event_type: eventType,
      browser_ts: timestamp,
      dsp_data,
    };
  
    console.log("EVENT DATA:\n", eventData);
  }
  
  (function (win) {
    var win = win || window;
    // doc = win.document;
  
    let thisScript = null,
      thisScriptSrc = null;
  
    function findGameLoaderScript() {
      script = document.getElementById("gameLoaderScript");
      if (script) {
        thisScript = script;
        thisScriptSrc = script.getAttribute("src");
      }
  
      return thisScript;
    }
  
    function makeTarget(id, width, height) {
      let par = thisScript.parentNode;
      id = id || "adludio_" + rand();
      let style;
      if (width === "%" && height === "%") {
        style =
          "position:absolute;top:0px;left:0px;width:100%;height:100%;min-width:320px;min-height:480px;text-align:center;overflow:hidden;";
      } else {
        style =
          "position:absolute;top:0px;left:0px;width:" +
          width +
          "px;height:" +
          height +
          "px;overflow:hidden;";
      }
      let el = makeEl("div", ["style", style, "id", id]);
      par.insertBefore(el, thisScript);
      return el;
    }
  
    function loadadunit() {
      sendEvent("creative_loading_started");
  
      gameContainerID = "w" + Math.floor(1e10 * Math.random());
      gameContainer = makeTarget(gameContainerID, params.width, params.height);
  
      const fabricScript = makeEl("script", [
        "src",
        "https://wat.adludio.com/loaders/cda/fabric.min.js",
      ]);
  
      fabricScript.onload = function () {
        console.info("finished loading fabric");
  
        // Load the ADUnit ONLY after fabric has finished loading
        let [game_id, game_version] = params.game_key.split("/");
        const game_url = `https://s3.${params.region}.amazonaws.com/a.futureadlabs.com/games/${game_id}/${game_version}/game.js`;
  
        const ad = makeEl("script", ["src", game_url]);
        ad.onload = function () {
          console.info("finished loading ad unit");
          sendEvent("creative_loading_complete");
        };
        thisScript.appendChild(ad);
      };
  
      thisScript.appendChild(fabricScript);
    }
  
    (function () {
      if (!canvasIsSupported()) {
        sendEvent("canvas-not-supported", {});
        throw Error("Canvas is not supported!");
      }
  
      findGameLoaderScript();
      if (!thisScript) {
        sendEvent("script-not-found", {});
        throw new Error("Unable to locate script");
      }
  
      params = safeParse(thisScript.innerText.trim());
  
      if (!params) {
        sendEvent("dsp-data-parsing-error", {});
        throw new Error("Unable to parse json");
      } else {
        console.info(params);
      }
  
      if (!params.width && !params.height) {
        throw new Error("Width and height missing");
      }
      sendEvent("dom_loading_started");
  
      window.addEventListener("DOMContentLoaded", function () {
        sendEvent("dom_loading_interactive");
      });
  
    
        sendEvent("dom_loading_complete");
        loadadunit();
    
  
      window.BeforeUnloadEvent = function () {
        sendEvent("dom_unloaded");
      };
    })();
  })(window);