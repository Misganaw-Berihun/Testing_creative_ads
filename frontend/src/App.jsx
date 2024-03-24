import EventsMatcher from "./components/EventsMatcher";
import { useState } from "react";
import GameLoaderComponent from "./components/GameLoader";
import "./styles.css";

export default function App() {
  const [region, setRegion] = useState(null);
  const [game_key, setGame_key] = useState(null);

  return (
    <div>
      <h1>Testing Ad-units!</h1>
      <div className="frame">
        <GameLoaderComponent setRegion={setRegion} setGame_key={setGame_key} />
      </div>
      <div>
        <EventsMatcher region={region} game_key={game_key} />
      </div>
    </div>
  );
}
