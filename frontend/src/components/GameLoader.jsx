import React, { useEffect, useState } from "react";
import JsonFileUploader from "./JsonFileUploader";

const GameLoaderComponent = ({ setRegion, setGame_key }) => {
  const [jsonFile, setJsonFile] = useState(null);

  useEffect(() => {
    if (jsonFile) {
      const script = document.createElement("script");
      script.src = "dsp_tester.js";
      script.async = true;
      script.id = "gameLoaderScript";

      const data = JSON.stringify(jsonFile);
      script.innerText = data;

      setRegion(jsonFile["region"]);
      setGame_key(jsonFile["game_key"]);
      document.body.appendChild(script);

      return () => {
        document.body.removeChild(script);
      };
    }
  }, [jsonFile]);
  
   

  return (
    <div>
      <JsonFileUploader setJsonFile={setJsonFile} />
      {jsonFile && (
        <div style={{ width: "320px", height: "550px" }}>
        </div>
      )}
    </div>
  );
};

export default GameLoaderComponent;
