import React, { useState, useEffect } from "react";
import axios from "axios";

const EventSelector = ({ events, onSelectionChange }) => {
  const [selectedEvents, setSelectedEvents] = useState([]);
  const [nonReactiveEvents, setNonReactiveEvents] = useState([]);
  const [reactiveEvents, setReactiveEvents] = useState([]);

  useEffect(() => {
    const nonReactive = events
      .filter((event) => event.event_type === "non-reactive")
      .map((event) => event.action_type);
    const reactive = events
      .filter((event) => event.event_type === "reactive")
      .map((event) => event.action_type);

    setNonReactiveEvents(nonReactive);
    setReactiveEvents(reactive);
  }, [events]);

  const toggleEventSelection = (eventType) => {
    if (selectedEvents.includes(eventType)) {
      setSelectedEvents(selectedEvents.filter((event) => event !== eventType));
    } else {
      setSelectedEvents([...selectedEvents, eventType]);
    }
  };

  return (
    <div className="bg-gray-100 p-4 rounded-md">
      <h2 className="text-lg font-bold mb-4">Non-reactive Events:</h2>
      <div className="flex flex-wrap gap-2">
        {nonReactiveEvents.map((event, index) => (
          <span
            key={index}
            className="inline-block bg-gray-200 text-gray-800 px-3 py-1 rounded-full text-sm mr-2 mb-2"
          >
            {event}
          </span>
        ))}
      </div>

      <div>
        <h2 className="text-lg font-bold mb-4"> Select Events:</h2>
        </div>
      <div className="flex flex-wrap gap-2 mt-4">
        {reactiveEvents.map((event, index) => (
          <div key={index} className="flex items-center gap-1">
            <input
              type="checkbox"
              id={event}
              checked={selectedEvents.includes(event)}
              onChange={() => toggleEventSelection(event)}
              className="form-checkbox h-5 w-5 text-indigo-600"
            />
            <label htmlFor={event} className="text-gray-800">
              {event}
            </label>
          </div>
        ))}
      </div>
      <button
        onClick={() => onSelectionChange(selectedEvents)}
        className="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:bg-indigo-700 transition duration-300"
      >
        Apply
      </button>
    </div>
  );
};
const events = [
  { action_type: "dom_loading_started", event_type: "non-reactive" },
  { action_type: "dom_loading_interactive", event_type: "non-reactive" },
  { action_type: "dom_loading_complete", event_type: "non-reactive" },
  { action_type: "impression/rendered", event_type: "non-reactive" },
  { action_type: "viewed", event_type: "non-reactive" },
  { action_type: "creative_loading_started", event_type: "non-reactive" },
  { action_type: "creative_loading_complete", event_type: "non-reactive" },
  { action_type: "frame_change", event_type: "non-reactive" },
  { action_type: "creative_complete", event_type: "non-reactive" },
  { action_type: "mouse_click", event_type: "non-reactive" },
  { action_type: "play_again", event_type: "reactive" },
  { action_type: "engagement", event_type: "reactive" },
  { action_type: "interaction", event_type: "reactive" },
  { action_type: "clickthrough", event_type: "reactive" },
  { action_type: "video_start", event_type: "reactive" },
  { action_type: "video_elapsed_time", event_type: "reactive" },
  { action_type: "video_mute", event_type: "reactive" },
  { action_type: "video_unmute", event_type: "reactive" },
  { action_type: "video_pause", event_type: "reactive" },
  { action_type: "video_resume", event_type: "reactive" },
  { action_type: "video_skip", event_type: "reactive" },
  { action_type: "video_close", event_type: "reactive" },
  { action_type: "video_end", event_type: "reactive" },
  { action_type: "bio_answer", event_type: "reactive" },
  { action_type: "user_choice", event_type: "reactive" },
  { action_type: "mouse_hover", event_type: "reactive" },
];

const EventsMatcher = ({ region, game_key }) => {
  const [matchedEvents, setMatchedEvents] = useState([]);
  const [unmatchedEvents, setUnmatchedEvents] = useState([]);

  const handleSelectionChange = async (selectedEvents) => {
    try {
      console.log("selected events:", selectedEvents, region, game_key);
      const response = await axios.post(
        "http://127.0.0.1:8000/api/compare_events",
        selectedEvents, 
        {
          params: {
            region: region,
            game_key: game_key,
          }
        }
      );
      console.log("Matched events:", response.data.matched_events);
      setMatchedEvents(response.data.matched_events);
      setUnmatchedEvents(response.data.unmatched_events)
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="bg-gray-100 p-4 rounded-md">
      <EventSelector
        events={events}
        onSelectionChange={handleSelectionChange}
      />
      <h2 className="text-lg font-bold mb-4">Matched Events:</h2>
      <div className="flex flex-wrap gap-2">
        {matchedEvents.map((event, index) => (
          <span
            key={index}
            className="inline-block bg-gray-200 text-gray-800 px-3 py-1 rounded-full text-sm mr-2 mb-2"
          >
            {event}
          </span>
        ))}
      </div>
      <h2 className="text-lg font-bold mb-4">Unmatched Events:</h2>
      <div className="flex flex-wrap gap-2">
        {unmatchedEvents.map((event, index) => (
          <span
            key={index}
            className="inline-block bg-gray-200 text-gray-800 px-3 py-1 rounded-full text-sm mr-2 mb-2"
          >
            {event}
          </span>
        ))}
      </div>
    </div>
  );
};

export default EventsMatcher;
