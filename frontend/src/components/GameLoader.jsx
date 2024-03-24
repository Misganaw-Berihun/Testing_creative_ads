import React, { useEffect, useState } from "react";
import JsonFileUploader from "./JsonFileUploader";

const GameLoaderComponent = ({ setRegion, setGame_key }) => {
  const [jsonFile, setJsonFile] = useState(null);

  useEffect(() => {
    if (jsonFile) {
      const script = document.createElement("script");
      script.src = "https://wat.adludio.com/loaders/cda/dsp_tester.js";
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
        <div>
          <h3>Uploaded JSON Data:</h3>
          <pre>{JSON.stringify(jsonFile, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default GameLoaderComponent;
