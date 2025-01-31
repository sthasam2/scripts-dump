import fs from "fs";

// array to hashmap based on id
const hashMap = (jsonArr) =>
  jsonArr.reduce((acc, cur) => {
    acc[cur.id] = cur;
    return acc;
  }, {});

const readJSONFile = (file) => {
  return JSON.parse(fs.readFileSync(file, "utf8"));
};

const provinceHashMap = hashMap(
  readJSONFile(
    "./data/provinces.json",
  ),
);

const districtHashMap = hashMap(
  readJSONFile(
    "./data/districts.json",
  ),
);

const municipalitiesHashMap = hashMap(
  readJSONFile(
    "./data/municipalities.json",
  ),
);

const districtMuniciplaitiesHashMap = Object.keys(
  municipalitiesHashMap,
).reduce((acc, cur) => {
  const districtId = municipalitiesHashMap[cur].district_id;
  if (acc[districtId]) {
    acc[districtId]["municipalities"][cur] = municipalitiesHashMap[cur];
  } else {
    acc[districtId] = {
      ...districtHashMap[districtId],
      municipalities: {
        [cur]: municipalitiesHashMap[cur],
      },
    };
  }
  return acc;
}, {});

const provinceDistrictHashMap = Object.keys(districtHashMap).reduce(
  (acc, cur) => {
    const provinceId = districtHashMap[cur].province_id;
    if (acc[provinceId]) {
      acc[provinceId]["districts"][cur] = districtHashMap[cur];
    } else {
      acc[provinceId] = {
        ...provinceHashMap[provinceId],
        districts: {
          [cur]: districtHashMap[cur],
        },
      };
    }
    return acc;
  },
  {},
);

fs.writeFileSync(
  "./data/geoLocation.json",
  JSON.stringify(provinceDistrictHashMap),
);
