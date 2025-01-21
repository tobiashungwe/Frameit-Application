import React, { useState } from "react";
import { Box, Typography } from "@mui/material";
import FileUploader from "./FileUploader";
import ParameterSelector from "./ParameterSelector";
import SanitizedContentViewer from "../HomePage/SanitizedContentViewer";
import DocumentViewer from "../HomePage/DocumentViewer";
import useFileUpload from "../../hooks/useFileUpload";

const ActivitySetup = ({ t, staticGroups, staticTerrains, staticMaterials }) => {
  const [groupCount, setGroupCount] = useState("");
  const [terrain, setTerrain] = useState("");
  const [material, setMaterial] = useState("");

  const [sanitizedContent, setSanitizedContent] = useState("");
  const [originalContent, setOriginalContent] = useState("");
  const [useSanitizedContent, setUseSanitizedContent] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const [extractedMaterials, setExtractedMaterials] = useState([]);
  const [extractedGroups, setExtractedGroups] = useState([]);
  const [extractedTerrains, setExtractedTerrains] = useState([]);

  const { handleUploadFile } = useFileUpload({
    t,
    setExtractedMaterials,
    setExtractedGroups,
    setExtractedTerrains,
  });

  const handleFileUpload = (file) => {
    handleUploadFile(file, setSanitizedContent, setOriginalContent, setIsLoading);
  };

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        {t("labels.activity_setup")}
      </Typography>

      <FileUploader
        onUploadFile={handleFileUpload}
        t={t}
        useSanitizedContent={useSanitizedContent}
        setUseSanitizedContent={setUseSanitizedContent}
      />

      <Box sx={{ mt: 4 }}>
        {useSanitizedContent && sanitizedContent ? (
          <SanitizedContentViewer sanitizedContent={sanitizedContent} t={t}>
            <DocumentViewer sanitizedContent={sanitizedContent} t={t} />
          </SanitizedContentViewer>
        ) : originalContent ? (
          <DocumentViewer sanitizedContent={originalContent} />
        ) : (
          <Typography variant="caption">{t("messages.no_content_message")}</Typography>
        )}
      </Box>

      <ParameterSelector
        groupCount={groupCount}
        setGroupCount={setGroupCount}
        terrain={terrain}
        setTerrain={setTerrain}
        material={material}
        setMaterial={setMaterial}
        staticGroups={staticGroups}
        staticTerrains={staticTerrains}
        staticMaterials={staticMaterials}
        extractedGroups={extractedGroups}
        extractedTerrains={extractedTerrains}
        extractedMaterials={extractedMaterials}
        t={t}
      />
    </Box>
  );
};

export default ActivitySetup;
