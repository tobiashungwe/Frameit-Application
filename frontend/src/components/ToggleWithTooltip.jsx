import React from "react";
import { Tooltip, Switch, FormControlLabel, Box } from "@mui/material";

const ToggleWithTooltip = ({ useSanitizedContent, setUseSanitizedContent, t }) => {
    return (
        <Box>
            <Tooltip
                title={t(
                    "tooltips.sanitize_explanation",
                    "Sanitizing removes the theme of your uploaded document. This ensures the activity focuses on a clear goal and improves story generation."
                )}
                arrow
                placement="top"
            >
        <span>
          <FormControlLabel
              control={
                  <Switch
                      checked={useSanitizedContent}
                      onChange={(e) => setUseSanitizedContent(e.target.checked)}
                  />
              }
              label={t("labels.remove_theme", "Remove theme for a clearer activity")}
          />
        </span>
            </Tooltip>
        </Box>
    );
};

export default ToggleWithTooltip;
