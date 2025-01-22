import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import { Box } from "@mui/material";
import HistoryPanel from "../components/Editor/HistoryPanel";
import StoryEditor from "../components/Editor/StoryEditor";
import AccountButton from "../components/Editor/AccountButton";
import SaveButton from "../components/Editor/SaveButton";
import LogoHeader from "../components/Layout/LogoHeader";

const EditorScreen = () => {
  const location = useLocation();
  const initialStory = location.state?.story || "No story provided"; // Fallback if no story passed

  const [selectedStory, setSelectedStory] = useState(initialStory);
  const [storyHistory, setStoryHistory] = useState(["Story 1", "Story 2", "Story 3", "Story 4", "Story 5"]);

  const handleSelectStory = (story) => {
    setSelectedStory(story);
  };

  const handleEditStory = (e) => {
    setSelectedStory(e.target.value);
  };

  const handleDeleteStory = () => {
    setSelectedStory("");
  };

  const handleSaveStory = () => {
    alert("Story saved!");
    setStoryHistory((prev) => [...prev, selectedStory]);
  };

  const handleViewAccount = () => {
    alert("Navigate to account view!");
  };

  return (
    <Box>
      <LogoHeader />
      <Box sx={{ display: "flex", gap: 2, p: 2 }}>
        {/* History Panel */}
        <Box sx={{ display: "flex", flexDirection: "column", width: "20%" }}>
          <HistoryPanel stories={storyHistory} onSelect={handleSelectStory} />
          <AccountButton onClick={handleViewAccount} />
        </Box>

        {/* Story Editor */}
        <Box sx={{ flexGrow: 1 }}>
          <StoryEditor
            story={selectedStory}
            onEdit={handleEditStory}
            onDelete={handleDeleteStory}
          />
          <SaveButton onSave={handleSaveStory} />
        </Box>
      </Box>
    </Box>
  );
};

export default EditorScreen;
