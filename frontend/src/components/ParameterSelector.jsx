import React from "react";
import { TextField, Typography, MenuItem, Box } from "@mui/material";
import Grid from '@mui/material/Grid2';

const ParameterSelector = ({
                             groupCount,
                             setGroupCount,
                             terrain,
                             setTerrain,
                             material,
                             setMaterial,
                             staticGroups,
                             staticTerrains,
                             staticMaterials,
                             t,
                           }) => {
  return (
      <>
        <Grid container spacing={2} mt={2} disableEqualOverflow>
          <Grid size={6}>
            <Typography variant="h6">{t("labels.groups")}</Typography>
            <TextField
                select
                value={groupCount}
                onChange={(e) => setGroupCount(e.target.value)}
                label={t("placeholders.select_groups")}
                fullWidth
            >
              {staticGroups.map((group) => (
                  <MenuItem key={group} value={group}>
                    {group}
                  </MenuItem>
              ))}
            </TextField>
          </Grid>

          <Grid size={6}>
            <Typography variant="h6">{t("labels.terrain")}</Typography>
            <TextField
                select
                value={terrain}
                onChange={(e) => setTerrain(e.target.value)}
                label={t("placeholders.select_terrain")}
                fullWidth
            >
              {staticTerrains.map((trn) => (
                  <MenuItem key={trn} value={trn}>
                    {trn}
                  </MenuItem>
              ))}
            </TextField>
          </Grid>
        </Grid>

        <Box mt={2}>
          <Typography variant="h6">{t("labels.materials")}</Typography>
          <TextField
              select
              value={material}
              onChange={(e) => setMaterial(e.target.value)}
              label={t("placeholders.select_material")}
              fullWidth
          >
            {staticMaterials.map((mat) => (
                <MenuItem key={mat} value={mat}>
                  {mat}
                </MenuItem>
            ))}
          </TextField>
        </Box>
      </>
  );
};

export default ParameterSelector;
