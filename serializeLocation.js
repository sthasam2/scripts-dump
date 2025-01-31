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
    "/home/sthasam/Programming/Work/Freelance/AutoEcommerce/auto-ecommerce-backend/data/provinces.json",
  ),
);

const districtHashMap = hashMap(
  readJSONFile(
    "/home/sthasam/Programming/Work/Freelance/AutoEcommerce/auto-ecommerce-backend/data/districts.json",
  ),
);

const municipalitiesHashMap = hashMap(
  readJSONFile(
    "/home/sthasam/Programming/Work/Freelance/AutoEcommerce/auto-ecommerce-backend/data/municipalities.json",
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
  "/home/sthasam/Programming/Work/Freelance/AutoEcommerce/auto-ecommerce-backend/data/geoLocation.json",
  JSON.stringify(provinceDistrictHashMap),
);
